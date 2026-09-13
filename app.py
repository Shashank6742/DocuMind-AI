import streamlit as st

from document_loader import extract_text_from_pdf
from rag_pipeline import RAGPipeline


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DOCUMIND AI — OBSIDIAN GOLD THEME
# ============================================================

st.markdown(
    """
<style>

    /* ========================================================
       GLOBAL APPLICATION
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 5%,
                rgba(245, 158, 11, 0.10),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 85%,
                rgba(234, 88, 12, 0.08),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #080808 0%,
                #12100d 48%,
                #0a0a0a 100%
            );

        color: #f5f0e6;
    }


    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0b0b0b 0%,
                #15120d 55%,
                #0c0c0c 100%
            );

        border-right: 1px solid #332a1c;
    }


    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #f7ead0;
    }


    section[data-testid="stSidebar"] p {
        color: #a09683;
    }


    section[data-testid="stSidebar"] hr {
        border-color: #332a1c;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;

        overflow: hidden;

        padding: 40px 44px;

        border-radius: 27px;

        background:
            linear-gradient(
                135deg,
                #17120b 0%,
                #25190a 45%,
                #15110c 100%
            );

        border: 1px solid #5b421b;

        box-shadow:
            0 20px 65px rgba(
                0,
                0,
                0,
                0.45
            ),
            inset 0 1px 0 rgba(
                255,
                190,
                60,
                0.08
            );

        margin-bottom: 26px;
    }


    .hero::before {
        content: "";

        position: absolute;

        width: 300px;
        height: 300px;

        right: -100px;
        top: -150px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(245, 158, 11, 0.28),
                transparent 70%
            );
    }


    .hero::after {
        content: "";

        position: absolute;

        width: 210px;
        height: 210px;

        left: 45%;
        bottom: -150px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(234, 88, 12, 0.16),
                transparent 70%
            );
    }


    .brand {
        position: relative;

        z-index: 2;

        font-size: 43px;

        font-weight: 850;

        letter-spacing: -1.8px;

        color: #fff7e5;

        margin-bottom: 9px;
    }


    .brand-accent {
        background:
            linear-gradient(
                90deg,
                #f59e0b,
                #ffd166,
                #fb923c
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    .tagline {
        position: relative;

        z-index: 2;

        font-size: 15px;

        color: #aaa08d;

        margin-bottom: 19px;
    }


    .status {
        position: relative;

        z-index: 2;

        display: inline-block;

        padding: 8px 15px;

        border-radius: 30px;

        background:
            rgba(
                245,
                158,
                11,
                0.09
            );

        border: 1px solid #76551c;

        color: #ffc857;

        font-size: 11px;

        font-weight: 750;

        letter-spacing: 0.5px;
    }


    /* ========================================================
       STAT CARDS
       ======================================================== */

    .stat-card {
        position: relative;

        overflow: hidden;

        background:
            linear-gradient(
                145deg,
                #181613,
                #11100e
            );

        border: 1px solid #382f22;

        border-radius: 20px;

        padding: 22px;

        min-height: 120px;

        box-shadow:
            0 12px 35px rgba(
                0,
                0,
                0,
                0.30
            );

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stat-card:hover {
        transform: translateY(-3px);

        border-color: #73531d;

        box-shadow:
            0 16px 40px rgba(
                0,
                0,
                0,
                0.40
            );
    }


    .stat-icon {
        font-size: 22px;

        margin-bottom: 7px;
    }


    .stat-number {
        font-size: 30px;

        font-weight: 850;

        color: #fff1c9;
    }


    .stat-label {
        font-size: 12px;

        color: #918979;

        margin-top: 3px;
    }


    /* ========================================================
       WELCOME CARD
       ======================================================== */

    .welcome {
        position: relative;

        overflow: hidden;

        text-align: center;

        padding: 65px 35px;

        margin-top: 25px;

        background:
            linear-gradient(
                145deg,
                #181613,
                #1a150e,
                #11100e
            );

        border-radius: 25px;

        border: 1px solid #3c3223;

        box-shadow:
            0 15px 50px rgba(
                0,
                0,
                0,
                0.32
            );
    }


    .welcome::before {
        content: "";

        position: absolute;

        width: 240px;
        height: 240px;

        left: -120px;
        top: -120px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(245, 158, 11, 0.14),
                transparent 70%
            );
    }


    .welcome::after {
        content: "";

        position: absolute;

        width: 220px;
        height: 220px;

        right: -120px;
        bottom: -120px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(234, 88, 12, 0.11),
                transparent 70%
            );
    }


    .welcome-icon {
        position: relative;

        z-index: 2;

        font-size: 56px;

        margin-bottom: 14px;
    }


    .welcome-title {
        position: relative;

        z-index: 2;

        font-size: 29px;

        font-weight: 800;

        color: #fff3d3;

        margin-bottom: 10px;
    }


    .welcome-text {
        position: relative;

        z-index: 2;

        color: #9d9585;

        font-size: 14px;

        line-height: 1.8;

        max-width: 700px;

        margin-left: auto;

        margin-right: auto;
    }


    /* ========================================================
       SOURCE CARDS
       ======================================================== */

    .source-card {
        background:
            linear-gradient(
                135deg,
                #1a1713,
                #12110f
            );

        border: 1px solid #3a3022;

        border-left: 4px solid #f59e0b;

        border-radius: 15px;

        padding: 16px 18px;

        margin-top: 11px;

        box-shadow:
            0 8px 25px rgba(
                0,
                0,
                0,
                0.25
            );
    }


    .source-title {
        font-weight: 750;

        color: #f0e5ce;

        font-size: 13px;
    }


    .source-page {
        display: inline-block;

        margin-top: 8px;

        padding: 4px 10px;

        border-radius: 8px;

        background:
            rgba(
                245,
                158,
                11,
                0.10
            );

        color: #ffc857;

        font-size: 11px;

        font-weight: 750;
    }


    .source-preview {
        margin-top: 9px;

        color: #918a7c;

        font-size: 12px;

        line-height: 1.6;
    }


    /* ========================================================
       DOCUMENT ITEMS
       ======================================================== */

    .document-item {
        background:
            linear-gradient(
                135deg,
                #171513,
                #12110e
            );

        border: 1px solid #352d22;

        border-radius: 12px;

        padding: 10px;

        margin-bottom: 7px;

        color: #b8ad98;

        font-size: 12px;

        box-shadow:
            0 5px 15px rgba(
                0,
                0,
                0,
                0.15
            );
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        background:
            #151311;

        border-radius: 14px;

        border: 1px solid #3b3021;

        padding: 5px;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        border-radius: 11px;

        border: 1px solid #4c3b21;

        background:
            linear-gradient(
                135deg,
                #201a11,
                #15130f
            );

        color: #d9ccb4;

        font-weight: 650;

        transition:
            all 0.2s ease;
    }


    .stButton > button:hover {
        border-color: #c0841a;

        color: #ffc857;

        background:
            linear-gradient(
                135deg,
                #2a2011,
                #1c170e
            );

        box-shadow:
            0 5px 18px rgba(
                245,
                158,
                11,
                0.10
            );
    }


    /* ========================================================
       CHAT
       ======================================================== */

    div[data-testid="stChatMessage"] {
        border-radius: 18px;
    }


    /* ========================================================
       CHAT & CHAT INPUT — OBSIDIAN GOLD
       ======================================================== */

    div[data-testid="stChatMessage"] {
        border-radius: 18px !important;
        background: transparent !important;
    }

    div[data-testid="stChatMessage"] p,
    div[data-testid="stChatMessage"] li {
        color: #f5f0e6 !important;
        font-size: 15px !important;
        line-height: 1.8 !important;
    }

    div[data-testid="stChatMessage"] strong {
        color: #ffd166 !important;
    }

    div[data-testid="stChatMessage"] h1,
    div[data-testid="stChatMessage"] h2,
    div[data-testid="stChatMessage"] h3 {
        color: #ffc857 !important;
    }

    /* FIX WHITE BOTTOM AREA */
    [data-testid="stBottom"] {
        background: #0b0b0b !important;
        background-color: #0b0b0b !important;
        border: none !important;
    }

    [data-testid="stBottom"] > div {
        background: #0b0b0b !important;
    }

    /* CHAT INPUT */
    [data-testid="stChatInput"] {
        background: #17130d !important;
        border: 1px solid #8a5a00 !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.55) !important;
    }

    [data-testid="stChatInput"] > div {
        background: #17130d !important;
        border-radius: 16px !important;
    }

    [data-testid="stChatInput"] textarea {
        background: #17130d !important;
        color: #fff7e5 !important;
        -webkit-text-fill-color: #fff7e5 !important;
        caret-color: #ffc857 !important;
        font-size: 14px !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #9d917d !important;
        -webkit-text-fill-color: #9d917d !important;
        opacity: 1 !important;
    }

    [data-testid="stChatInput"] button {
        background: #ffb52e !important;
        color: #17130d !important;
        border: none !important;
        border-radius: 10px !important;
    }

    [data-testid="stChatInput"] button:hover {
        background: #ffd166 !important;
    }
    /* ========================================================
       FOOTER
       ======================================================== */

    .app-footer {
        text-align: center;

        color: #746c5c;

        font-size: 11px;

        margin-top: 35px;

        padding-bottom: 15px;
    }

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "rag" not in st.session_state:
    st.session_state.rag = RAGPipeline()


if "documents" not in st.session_state:
    st.session_state.documents = {}


if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 📚 Document Library"
    )

    st.caption(
        "Turn your academic PDFs into an "
        "intelligent knowledge base."
    )

    st.divider()


    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload one or more academic PDF documents."
    )


    if uploaded_files:

        for uploaded_file in uploaded_files:

            file_name = uploaded_file.name


            if file_name not in st.session_state.documents:

                with st.spinner(
                    f"Processing {file_name}..."
                ):

                    pages = extract_text_from_pdf(
                        uploaded_file
                    )


                    chunk_count = (
                        st.session_state.rag.add_document(
                            pages,
                            file_name
                        )
                    )


                    if chunk_count > 0:

                        st.session_state.documents[
                            file_name
                        ] = {
                            "pages": len(pages),
                            "chunks": chunk_count
                        }

                        st.success(
                            f"✓ {file_name}"
                        )

                    else:

                        st.error(
                            f"No readable text found "
                            f"in {file_name}."
                        )


    st.divider()


    # ========================================================
    # KNOWLEDGE BASE
    # ========================================================

    st.markdown(
        "### 🧠 Knowledge Base"
    )


    document_count = len(
        st.session_state.documents
    )


    page_count = sum(
        document["pages"]
        for document
        in st.session_state.documents.values()
    )


    chunk_count = len(
        st.session_state.rag.chunks
    )


    st.write(
        f"📄 **Documents:** {document_count}"
    )


    st.write(
        f"📑 **Pages:** {page_count}"
    )


    st.write(
        f"🧩 **Chunks:** {chunk_count}"
    )


    # ========================================================
    # DOCUMENT LIST
    # ========================================================

    if document_count > 0:

        st.divider()

        st.markdown(
            "### 📂 Your Documents"
        )


        for file_name in list(
            st.session_state.documents.keys()
        ):

            col1, col2 = st.columns(
                [5, 1]
            )


            with col1:

                st.markdown(
                    f"""
<div class="document-item">
📄 {file_name}
</div>
""",
                    unsafe_allow_html=True
                )


            with col2:

                if st.button(
                    "×",
                    key=f"remove_{file_name}"
                ):

                    st.session_state.rag.remove_document(
                        file_name
                    )

                    del st.session_state.documents[
                        file_name
                    ]

                    st.rerun()


    st.divider()


    if st.button(
        "🗑️ Clear Knowledge Base",
        use_container_width=True
    ):

        st.session_state.rag.clear()

        st.session_state.documents = {}

        st.session_state.messages = []

        st.rerun()


# ============================================================
# HERO SECTION
# ============================================================

st.html(
    """
<div class="hero">

    <div class="brand">
        🧠 <span class="brand-accent">DocuMind AI</span>
    </div>

    <div class="tagline">
        Ask questions. Explore knowledge.
        Get answers grounded in your documents.
    </div>

    <span class="status">
    ● DOCUMENT-GROUNDED AI &nbsp;•&nbsp; READY
    </span>

</div>
"""
)


# ============================================================
# STATISTICS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.html(
        f"""
<div class="stat-card">

    <div class="stat-icon">
        📄
    </div>

    <div class="stat-number">
        {document_count}
    </div>

    <div class="stat-label">
        Documents
    </div>

</div>
"""
    )


with col2:

    st.html(
        f"""
<div class="stat-card">

    <div class="stat-icon">
        📑
    </div>

    <div class="stat-number">
        {page_count}
    </div>

    <div class="stat-label">
        Pages Indexed
    </div>

</div>
"""
    )


with col3:

    st.html(
        f"""
<div class="stat-card">

    <div class="stat-icon">
        🧩
    </div>

    <div class="stat-number">
        {chunk_count}
    </div>

    <div class="stat-label">
        Knowledge Chunks
    </div>

</div>
"""
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:

    if document_count == 0:

        st.html(
            """
<div class="welcome">

    <div class="welcome-icon">
        🧠
    </div>

    <div class="welcome-title">
        Your Academic Knowledge, Reimagined
    </div>

    <p class="welcome-text">
        Upload your academic PDFs from the sidebar
        and transform them into an intelligent,
        searchable knowledge base.
        Ask questions naturally and receive answers
        grounded in your uploaded documents.
    </p>

</div>
"""
        )

    else:

        st.html(
            """
<div class="welcome">

    <div class="welcome-icon">
        ✨
    </div>

    <div class="welcome-title">
        Your Knowledge Base Is Ready
    </div>

    <p class="welcome-text">
        Your documents have been indexed successfully.
        Ask a question below and DocuMind AI will
        retrieve the most relevant information before
        generating a grounded answer.
    </p>

</div>
"""
        )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


        if message.get("sources"):

            st.markdown(
                "### 📚 Sources"
            )


            displayed_sources = set()


            for source in message["sources"]:

                source_key = (
                    source["document"],
                    source["page"]
                )


                if source_key in displayed_sources:
                    continue


                displayed_sources.add(
                    source_key
                )


                st.html(
                    f"""
<div class="source-card">

    <div class="source-title">
        📄 {source["document"]}
    </div>

    <span class="source-page">
        Page {source["page"]}
    </span>

    <div class="source-preview">
        {source["text"][:300]}...
    </div>

</div>
"""
                )


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask anything about your uploaded documents..."
)


if question:

    if not st.session_state.rag.chunks:

        st.warning(
            "📄 Please upload at least one PDF "
            "before asking a question."
        )

    else:

        # ----------------------------------------------------
        # USER MESSAGE
        # ----------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message(
            "user"
        ):

            st.markdown(
                question
            )


        # ----------------------------------------------------
        # RETRIEVAL
        # ----------------------------------------------------

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "🔎 Searching your knowledge base..."
            ):

                results = (
                    st.session_state.rag.search(
                        question,
                        top_k=5
                    )
                )


            # ------------------------------------------------
            # ANSWER GENERATION
            # ------------------------------------------------

            with st.spinner(
                "🧠 Generating grounded answer..."
            ):

                answer = (
                    st.session_state.rag.generate_answer(
                        question,
                        results
                    )
                )


            st.markdown(
                answer
            )


            # ------------------------------------------------
            # SOURCES
            # ------------------------------------------------

            if results:

                st.markdown(
                    "### 📚 Sources"
                )


                displayed_sources = set()


                for source in results:

                    source_key = (
                        source["document"],
                        source["page"]
                    )


                    if source_key in displayed_sources:
                        continue


                    displayed_sources.add(
                        source_key
                    )


                    st.html(
                        f"""
<div class="source-card">

    <div class="source-title">
        📄 {source["document"]}
    </div>

    <span class="source-page">
        Page {source["page"]}
    </span>

    <div class="source-preview">
        {source["text"][:300]}...
    </div>

</div>
"""
                    )


        # ----------------------------------------------------
        # SAVE ASSISTANT MESSAGE
        # ----------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": results
            }
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
<div class="app-footer">
    DocuMind AI · Academic RAG Knowledge Assistant
    · Intelligent document exploration
</div>
"""
)