from pathlib import Path

# Project paths

BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "documents"

VECTOR_STORE_DIR = BASE_DIR / "vector_store"

UPLOADS_DIR = BASE_DIR / "uploads"

RESULTS_DIR = BASE_DIR / "results"

# Ollama configuration

OLLAMA_URL = "http://localhost:11434"

LLM_MODEL = "llama3.2:3b"

EMBEDDING_MODEL = "qwen3-embedding:0.6b"

# ChromaDB configuration

COLLECTION_NAME = "university_documents"

# RAG configuration

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

TOP_K = 5

for folder in [

    DOCUMENTS_DIR,

    VECTOR_STORE_DIR,

    UPLOADS_DIR,

    RESULTS_DIR

]:

    folder.mkdir(

        parents=True,

        exist_ok=True

    )