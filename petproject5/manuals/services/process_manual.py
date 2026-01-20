from .loader import load_document
from .chanker import split_documents
from .vector_store import build_vector_store


def process_manual(device):
    documents = load_document(device.manual.path)
    chunks = split_documents(documents)
    build_vector_store(device.id, chunks)
    device.has_embeddings = True
    device.save(update_fields=["has_embeddings"])
