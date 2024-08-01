def initialize_llm():
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm_pipeline = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.3
    )
    return llm_pipeline
