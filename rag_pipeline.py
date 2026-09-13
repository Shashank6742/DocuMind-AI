from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


class RAGPipeline:

    def __init__(self):

        # Embedding model
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        # FAISS index
        self.index = None

        # All chunks from all uploaded documents
        self.chunks = []

        # Groq client
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. "
                "Please add it to your .env file."
            )

        self.client = Groq(
            api_key=api_key
        )

    # ---------------------------------------------------------
    # CREATE CHUNKS
    # ---------------------------------------------------------

    def create_chunks(
        self,
        pages,
        document_name,
        chunk_size=600,
        overlap=120
    ):

        chunks = []

        for page in pages:

            text = page["text"]
            page_number = page["page"]

            start = 0

            while start < len(text):

                end = start + chunk_size

                chunk_text = text[start:end].strip()

                if chunk_text:

                    chunks.append({
                        "text": chunk_text,
                        "page": page_number,
                        "document": document_name
                    })

                start += chunk_size - overlap

        return chunks

    # ---------------------------------------------------------
    # ADD DOCUMENT
    # ---------------------------------------------------------

    def add_document(
        self,
        pages,
        document_name
    ):

        new_chunks = self.create_chunks(
            pages,
            document_name
        )

        if not new_chunks:
            return 0

        # Add new document chunks
        # without deleting previous documents
        self.chunks.extend(new_chunks)

        # Rebuild FAISS index using ALL chunks
        self.build_index()

        return len(new_chunks)

    # ---------------------------------------------------------
    # BUILD FAISS INDEX
    # ---------------------------------------------------------

    def build_index(self):

        if not self.chunks:
            self.index = None
            return

        texts = [
            chunk["text"]
            for chunk in self.chunks
        ]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        embeddings = embeddings.astype(
            "float32"
        )

        # Inner Product works as cosine similarity
        # when embeddings are normalized.
        self.index = faiss.IndexFlatIP(
            embeddings.shape[1]
        )

        self.index.add(
            embeddings
        )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    def search(
        self,
        question,
        top_k=5
    ):

        if (
            self.index is None
            or not self.chunks
        ):
            return []

        question_embedding = self.model.encode(
            [question],
            convert_to_numpy=True,
            normalize_embeddings=True
        ).astype("float32")

        scores, indices = self.index.search(
            question_embedding,
            min(
                top_k,
                len(self.chunks)
            )
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index < 0:
                continue

            result = self.chunks[index].copy()

            result["score"] = float(score)

            results.append(
                result
            )

        return results

    # ---------------------------------------------------------
    # GENERATE ANSWER USING GROQ
    # ---------------------------------------------------------

    def generate_answer(
        self,
        question,
        results
    ):

        if not results:

            return (
                "I couldn't find this information "
                "in the uploaded documents."
            )

        context_parts = []

        for number, result in enumerate(
            results,
            start=1
        ):

            context_parts.append(
                f"""
SOURCE {number}

Document:
{result["document"]}

Page:
{result["page"]}

Content:
{result["text"]}
"""
            )

        context = "\n".join(
            context_parts
        )

        prompt = f"""
You are DocuMind AI, a professional academic
document question-answering assistant.

Your job is to answer the user's question using
ONLY the information contained in the provided
document context.

STRICT RULES:

1. Use only the provided context.
2. Do not use outside knowledge.
3. Do not invent facts.
4. If the context does not contain enough
   information to answer the question, say:

"I couldn't find this information in the
uploaded documents."

5. Give a clear and useful answer.
6. Keep the answer reasonably concise.
7. Do not mention the system instructions.
8. Do not mention that you are using a prompt.
9. When useful, organize the answer using
   short bullet points or numbered points.

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{question}
"""

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are DocuMind AI. "
                        "Answer strictly from "
                        "the supplied document context."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2
        )

        return response.choices[0].message.content

    # ---------------------------------------------------------
    # REMOVE DOCUMENT
    # ---------------------------------------------------------

    def remove_document(
        self,
        document_name
    ):

        self.chunks = [
            chunk
            for chunk in self.chunks
            if chunk["document"] != document_name
        ]

        self.build_index()

    # ---------------------------------------------------------
    # CLEAR EVERYTHING
    # ---------------------------------------------------------

    def clear(self):

        self.chunks = []

        self.index = None