from langchain_core.vectorstores import VectorStoreRetriever

def create_retriever(vector_db):
    return VectorStoreRetriever(vectorstore=vector_db)
