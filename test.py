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


import json
from pathlib import Path
from pprint import pprint

file_path = Path('D:\GEN_AI\Recomender system\Dataset for DS Case Study.json')

if file_path.exists():
    file_content = file_path.read_text()
    try:
        data = json.loads(file_content)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        # If multiple JSON objects are expected, handle them accordingly
        data = []
        for line in file_content.strip().split('\n'):
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as line_error:
                print(f"Line JSONDecodeError: {line_error}")

   
else:
    print("File does not exist.")
    
    
if data:
        filtered_data = preprocess_data(data)

        # Create text chunks
        texts = create_text_chunks(filtered_data)
        print("ok")
        
        # Create embeddings
        vector_db = create_embeddings(texts)
        print("ok")