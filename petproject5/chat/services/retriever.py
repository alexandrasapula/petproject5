from manuals.services.vector_store import load_vector_store


def get_device_retriever(device_id, k=5):
    vectorstore = load_vector_store(device_id)
    if not vectorstore:
        return None
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})
