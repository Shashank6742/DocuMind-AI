# 🧠 DocuMind AI

### Academic Knowledge & Student Assistant

DocuMind AI is a domain-specific Retrieval-Augmented Generation (RAG) chatbot designed to answer questions from uploaded academic PDF documents.

It combines document processing, semantic search, vector embeddings, FAISS, and a Large Language Model to provide document-grounded answers with source and page references.

## ✨ Features

- 📄 Upload one or multiple academic PDF documents
- 🔍 Extract text from PDF pages
- ✂️ Split documents into searchable knowledge chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- ⚡ Store and search embeddings using FAISS
- 💬 Ask natural-language questions about uploaded documents
- 🤖 Generate answers using a Groq-powered LLM
- 📚 Display source documents and page references
- 🚫 Avoid unsupported answers when information is not present
- 🗂️ Manage uploaded documents
- 🧹 Clear the knowledge base when required
- 🎨 Professional dark gold/orange Streamlit interface

## 🏗️ System Architecture

```text
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Sentence Transformer Embeddings
      ↓
FAISS Vector Database
      ↓
User Question
      ↓
Semantic Similarity Search
      ↓
Top Relevant Chunks
      ↓
Groq LLM
      ↓
Grounded Answer + Source References
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
PyPDF	PDF text extraction
Sentence Transformers	Semantic text embeddings
FAISS	Vector similarity search
NumPy	Numerical processing
Groq	Large Language Model
python-dotenv	Environment variable management
📁 Project Structure
DocuMind-AI/
│
├── assets/
│   ├── home.png
│   ├── question-answer.png
│   ├── multiple-sources.png
│   └── refusal-test.png
│
├── app.py
├── document_loader.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the Repository
git clone https://github.com/Shashank6742/DocuMind-AI.git
cd DocuMind-AI
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment

For Command Prompt:

venv\Scripts\activate
4. Install Required Packages
pip install -r requirements.txt
🔑 Groq API Configuration

Create a .env file in the project folder:

GROQ_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

▶️ Run the Application
streamlit run app.py

The application will open in your browser.

💡 How to Use
Launch DocuMind AI.
Upload one or more academic PDF documents.
The documents are processed and indexed.
Enter a question related to the uploaded documents.
DocuMind AI retrieves the most relevant information.
The LLM generates a grounded response.
Source documents and page references are displayed with the answer.
If the information is not available, the system informs the user instead of inventing an answer.
🧪 Testing

The application was tested using both document-related and out-of-document questions.

Test 1 — Document-Based Question

Question: What is Big Data?

The system retrieves relevant information from the uploaded academic document and generates a grounded answer with source references.

Test 2 — Classification Question

Question: What are the three categories of digital data?

The system identifies the relevant document sections and displays the answer with page references.

Test 3 — Out-of-Document Question

Question: What is the capital of Japan?

Since the information is not available in the uploaded document, the system responds that the information could not be found instead of generating an unsupported answer.

📸 Project Screenshots
🏠 Home Interface

The main interface provides PDF upload, knowledge-base statistics, document management, and the DocuMind AI chat interface.

💬 Document-Grounded Question Answering

The chatbot retrieves relevant information from the uploaded academic document and generates a grounded answer.

📚 Retrieved Sources and Page References

Relevant document chunks are displayed with their source document and page references.

🚫 Out-of-Document Question Handling

When the requested information is not available in the uploaded documents, DocuMind AI avoids generating an unsupported answer.

🔒 Privacy and Security
API keys are stored using environment variables.
.env is excluded from version control.
Uploaded documents are processed for the application's knowledge base.
The chatbot is designed to ground answers in the uploaded documents.
🚀 Future Enhancements
Conversation memory
Multiple knowledge-base collections
Document summarization
User feedback system
Improved retrieval ranking
Support for additional document formats
Deployment as a cloud application
🎓 Academic Project

Project: DocuMind AI — Academic Knowledge & Student Assistant

Domain: Artificial Intelligence / Natural Language Processing / Retrieval-Augmented Generation

Purpose: Domain-specific question answering from academic PDF documents.