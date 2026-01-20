from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    TextLoader
)


def load_document(path: str):
    ext = Path(path).suffix.lower()

    if ext == ".pdf":
        return PyPDFLoader(path).load()

    elif ext == ".docx":
        return UnstructuredWordDocumentLoader(path).load()

    elif ext == ".txt":
        return TextLoader(path, encoding="utf-8").load()

    else:
        raise ValueError(f"Unsupported file type: {ext}")