from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
