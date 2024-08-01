from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def create_chains(llm_pipeline, prompt, retriever):
    document_chain = create_stuff_documents_chain(llm_pipeline, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    return retrieval_chain
