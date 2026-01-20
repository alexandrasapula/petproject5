from pathlib import Path
from langchain_community.vectorstores import FAISS
from .embedding import get_embedding_model


BASE_DIR = Path(__file__).resolve().parents[3]
VECTOR_DB_DIR = BASE_DIR / "vector_db"
VECTOR_DB_DIR.mkdir(exist_ok=True)


def build_vector_store(device_id: int, documents):
    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    path = VECTOR_DB_DIR / f"device_{device_id}"
    vector_store.save_local(path)

    return path


def load_vector_store(device_id: int):
    embeddings = get_embedding_model()
    path = VECTOR_DB_DIR / f"device_{device_id}"

    if not path.exists():
        return None

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
