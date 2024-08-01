import os
from dotenv import load_dotenv
from src.data_loader import load_json
import google.generativeai as genai
from src.preprocessor import preprocess_data
from src.text_splitter import create_text_chunks
from src.embedding import create_embeddings
from src.retriever import create_retriever
from src.prompt_template import create_prompt_template
from src.chain import create_chains
from utils import initialize_llm



# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# os.getenv['GOOGLE_API_KEY'] = GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

def main():
    
    
    # Load and preprocess data
    data = load_json('D:\GEN_AI\Recomender system\Dataset for DS Case Study.json')
    if data:
        filtered_data = preprocess_data(data)

        # Create text chunks
        texts = create_text_chunks(filtered_data)

        # Create embeddings
        vector_db = create_embeddings(texts)

        # Create retriever
        retriever = create_retriever(vector_db)

        # Initialize LLM
        llm_pipeline = initialize_llm()

        # Create prompt template
        prompt = create_prompt_template()

        # Create chains
        retrieval_chain = create_chains(llm_pipeline, prompt, retriever)

        # Get response
        response = retrieval_chain.invoke({"input": "B00002243X"})
        print(response['answer'])

if __name__ == "__main__":
    main()
