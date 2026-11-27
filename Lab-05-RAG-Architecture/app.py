
import streamlit as st

from ingest import (
    ingest_pdf,
    list_documents,
    build_vector_store
)

from rag_pipeline import ask_university


# Page configuration
st.set_page_config(
    page_title="University AI Assistant",
    page_icon="🎓",
    layout="wide"
)


# Main heading
st.title("🎓 University AI Assistant")

st.caption(
    "Document-based University Knowledge System"
)

st.divider()


# Initialize chat history
if "messages" not in st.session_state:

    st.session_state.messages = []


# Display source references
def display_sources(sources):

    if sources:

        with st.expander("View Retrieved Sources"):

            for i, source in enumerate(
                sources, start=1
            ):

                st.write(
                    f"[Source {i}] "
                    f"{source['document']} "
                    f"— Page {source['page']}"
                )


# Sidebar
with st.sidebar:

    st.header("📚 Knowledge Base")

    uploaded_files = st.file_uploader(
        "Upload university PDF documents",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button(
        "Process Documents",
        type="primary",
        use_container_width=True
    ):

        if uploaded_files:

            progress = st.progress(0)

            for i, uploaded_file in enumerate(
                uploaded_files
            ):

                try:

                    with st.spinner(
                        f"Processing {uploaded_file.name}..."
                    ):

                        message = ingest_pdf(uploaded_file)

                    st.success(message)

                except Exception as e:

                    st.error(
                        f"Failed: {uploaded_file.name} - {e}"
                    )

                progress.progress(
                    (i + 1) / len(uploaded_files)
                )

        else:

            st.warning("Please select PDF files first.")

    st.divider()

    # Rebuild vector database
    if st.button(
        "Rebuild Knowledge Base",
        use_container_width=True
    ):

        try:

            with st.spinner("Indexing documents..."):

                _, total_chunks = build_vector_store()

            st.success(
                f"Indexed {total_chunks} chunks."
            )

        except Exception as e:

            st.error(str(e))

    st.divider()

    # Stored documents
    st.subheader("Stored Documents")

    documents = list_documents()

    st.metric("Available PDFs", len(documents))

    if documents:

        for doc in documents:

            st.write(f"📄 {doc.name}")

    else:

        st.info("No PDFs stored yet.")

    st.divider()

    st.subheader("System Information")

    st.write("**Architecture:** RAG")
    st.write("**Language Model:** Llama 3.2")
    st.write("**Vector Database:** ChromaDB")
    st.write("**Model Provider:** Ollama")

    st.divider()

    if st.button(
        "Clear Chat History",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.rerun()


# Chat interface
st.header("💬 Ask the University Assistant")

if not st.session_state.messages:

    st.info(
        "Ask questions about university programmes, "
        "academic regulations, assessments, "
        "and graduation requirements."
    )


# Display conversation history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        display_sources(
            message.get("sources", [])
        )


# User question
question = st.chat_input(
    "Ask a question about the university..."
)


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):

        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching university documents..."
        ):

            try:

                result = ask_university(question)

                st.markdown(result["answer"])

                display_sources(result["sources"])

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                })

            except Exception as e:

                st.error(f"Error: {e}")
