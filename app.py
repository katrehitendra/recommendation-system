from flask import Flask, request, jsonify, render_template
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

app = Flask(__name__)

# Initialize components
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# os.getenv['GOOGLE_API_KEY'] = GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

data = load_json('Dataset for DS Case Study.json')
if data:
    filtered_data = preprocess_data(data)
    texts = create_text_chunks(filtered_data)
    vector_db = create_embeddings(texts)
else:
    vector_db = load_embeddings()

retriever = create_retriever(vector_db)
llm_pipeline = initialize_llm()
prompt = create_prompt_template()
retrieval_chain = create_chains(llm_pipeline, prompt, retriever)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    product_id = request.form.get('product_id')
    if product_id:
        response = retrieval_chain.invoke({"input": product_id})
        return jsonify(response['answer'])
    return jsonify({"error": "No product ID provided"})

if __name__ == "__main__":
    app.run(debug=True)
