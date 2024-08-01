import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os

def create_embeddings(texts):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_db = Chroma.from_documents(texts, embeddings)
    
    
    return vector_db

# def load_embeddings(persist_directory="chroma_store"):
#     embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
#     # Load the vectors and their metadata
#     with open(os.path.join(persist_directory, "vectors.json"), "r") as f:
#         data = json.load(f)
    
#     vector_db = Chroma.from_dict(data, embeddings)
#     return vector_db

