from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_text_chunks(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.create_documents(data)