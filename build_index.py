# build_index.py
import os
import logging
from dotenv import load_dotenv

# --- RAG Libraries ---
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings # Base class for UniversityEmbeddings if needed separately
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

from main import UniversityEmbeddings 
from config import full_knowledge_text 

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv() # Load environment variables from .env file

# --- Secrets & Settings ---
UNIVERSITY_API_KEY = os.getenv("UNIVERSITY_API_KEY")
if not UNIVERSITY_API_KEY:
    logging.error("UNIVERSITY_API_KEY not found in .env file.")
    exit(1)

# Reuse configuration from main.py if possible
UNIVERSITY_BASE_URL = "https://genai.hkbu.edu.hk/general/rest"
UNIVERSITY_EMBEDDING_MODEL_NAME = "text-embedding-3-large"
UNIVERSITY_API_VERSION = "2024-05-01-preview"
EMBEDDING_BATCH_SIZE = 16 # Match batch size used in main app

FAISS_INDEX_PATH = "faiss_index" # Directory where index files will be saved

def build_and_save_index():
    """Builds the FAISS index from the knowledge base and saves it locally."""
    logging.info("Initializing University Embeddings...")
    try:
        embeddings = UniversityEmbeddings(
            api_key=UNIVERSITY_API_KEY,
            base_url=UNIVERSITY_BASE_URL,
            model_name=UNIVERSITY_EMBEDDING_MODEL_NAME,
            api_version=UNIVERSITY_API_VERSION,
            embed_batch_size=EMBEDDING_BATCH_SIZE
        )
        logging.info("Embeddings client initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize University Embeddings client: {e}", exc_info=True)
        return

    if not full_knowledge_text:
        logging.error("Source text data (full_knowledge_text) is empty. Cannot build index.")
        return

    logging.info("Preparing documents...")
    docs = [Document(page_content=full_knowledge_text)]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    logging.info(f"Split data into {len(chunks)} chunks.")

    if not chunks:
        logging.error("No chunks were created. Cannot build index.")
        return

    try:
        logging.info("Creating FAISS index from documents... This may take a while.")
        # This step will call the embedding API for all chunks
        db = FAISS.from_documents(chunks, embeddings)
        logging.info("FAISS index created successfully.")

        logging.info(f"Saving FAISS index to: {FAISS_INDEX_PATH}")
        db.save_local(FAISS_INDEX_PATH)
        logging.info("FAISS index saved successfully.")
        logging.info(f"Index files saved: {FAISS_INDEX_PATH}/index.faiss, {FAISS_INDEX_PATH}/index.pkl")

    except Exception as e:
        logging.error(f"Error creating or saving FAISS index: {e}", exc_info=True)

if __name__ == "__main__":
    build_and_save_index()