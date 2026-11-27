
import hashlib
from pathlib import Path

import pymupdf

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from config import (
    DOCUMENTS_DIR,
    UPLOADS_DIR,
    VECTOR_STORE_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    OLLAMA_URL,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


# Create required directories
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)


# List available PDF documents
def list_documents():

    return sorted(
        list(DOCUMENTS_DIR.glob("*.pdf"))
        + list(UPLOADS_DIR.glob("*.pdf"))
    )


# Load PDF documents
def load_documents():

    documents = []
    pdf_files = list_documents()

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found. Add PDFs to the documents folder."
        )

    for pdf_path in pdf_files:

        print(f"Loading: {pdf_path.name}")

        with pymupdf.open(str(pdf_path)) as pdf:

            for page_number, page in enumerate(pdf):

                text = page.get_text().strip()

                if not text:
                    continue

                document = Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path.name,
                        "page": page_number + 1
                    }
                )

                documents.append(document)

    print(f"Loaded {len(documents)} pages.")

    return documents


# Split documents into chunks
def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = index

    print(f"Created {len(chunks)} text chunks.")

    return chunks


# Initialize Chroma vector database
def get_vector_store():

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_URL
    )

    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(VECTOR_STORE_DIR),
        embedding_function=embeddings
    )


# Build or update vector database
def build_vector_store():

    documents = load_documents()
    chunks = split_documents(documents)

    if not chunks:
        raise ValueError(
            "No readable text found in the PDF documents."
        )

    vector_store = get_vector_store()

    ids = []

    for chunk in chunks:

        raw_id = (
            f"{chunk.metadata['source']}:"
            f"{chunk.metadata['page']}:"
            f"{chunk.metadata['chunk_id']}:"
            f"{chunk.page_content}"
        )

        chunk_id = hashlib.sha256(
            raw_id.encode("utf-8")
        ).hexdigest()

        ids.append(chunk_id)

    old_ids = set(vector_store.get()["ids"])

    # Only embed new chunks
    new_chunks = []
    new_ids = []

    for chunk, chunk_id in zip(chunks, ids):

        if chunk_id not in old_ids:
            new_chunks.append(chunk)
            new_ids.append(chunk_id)

    if new_chunks:

        vector_store.add_documents(
            documents=new_chunks,
            ids=new_ids
        )

    # Remove obsolete chunks
    obsolete_ids = list(old_ids - set(ids))

    if obsolete_ids:
        vector_store.delete(ids=obsolete_ids)

    print("Vector database created successfully!")
    print("Vector database location:", VECTOR_STORE_DIR)
    print("Total indexed chunks:", len(ids))

    return vector_store, len(ids)


# Process uploaded PDF from Streamlit
def ingest_pdf(uploaded_file):

    filename = Path(uploaded_file.name).name

    if not filename.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are supported.")

    file_data = uploaded_file.getvalue()

    # Validate PDF before saving
    with pymupdf.open(
        stream=file_data,
        filetype="pdf"
    ) as pdf:

        if not any(page.get_text().strip() for page in pdf):
            raise ValueError(
                "The PDF contains no readable text."
            )

    file_path = UPLOADS_DIR / filename

    file_path.write_bytes(file_data)

    vector_store, total_chunks = build_vector_store()

    return (
        f"{filename} processed successfully. "
        f"Total indexed chunks: {total_chunks}"
    )


# Run ingestion directly
if __name__ == "__main__":

    build_vector_store()
