# main.py
import sys
import streamlit as st
import requests
import json
import os # Keep os for path checking
# import shutil # No longer needed
import logging
import time
from typing import List

# --- RAG Libraries ---
# REMOVE Chroma imports related to client/persistence if any remain
# from langchain_community.vectorstores import Chroma
# import chromadb
# from chromadb.config import Settings
# from chromadb.errors import CollectionNotFoundError

from langchain_community.vectorstores import FAISS # ADD FAISS import
from langchain_core.embeddings import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter # Keep if needed elsewhere, maybe not?
from langchain.docstore.document import Document # Keep if needed elsewhere, maybe not?


# --- Load Data from Config ---
from config import full_knowledge_text # Still needed for reference or maybe not? Decide if needed beyond index.

# --- Logging Configuration ---
log_level = logging.DEBUG
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
# log_file = 'chatbot.log' # Less useful in cloud

logging.basicConfig(level=log_level, format=log_format, stream=sys.stdout)
logger = logging.getLogger(__name__)


# --- Custom University Embedding Class (Keep as is) ---
class UniversityEmbeddings(Embeddings):
    # ... (Your existing UniversityEmbeddings class code - no changes needed here) ...
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model_name: str,
        api_version: str,
        embed_batch_size: int = 1
    ):
        # ... (rest of init) ...
        self.api_key = api_key
        # Construct the specific endpoint URL for embeddings
        self.endpoint_url = f"{base_url}/deployments/{model_name}/embeddings?api-version={api_version}"
        self.headers = {
            'Content-Type': 'application/json',
            'api-key': self.api_key
        }
        self.embed_batch_size = embed_batch_size # How many texts to send in one API call
        logger.info(f"Initialized UniversityEmbeddings with endpoint: {self.endpoint_url}")

    def _embed(self, texts: List[str]) -> List[List[float]]:
        # ... (Your _embed method) ...
        all_embeddings = []
        for i in range(0, len(texts), self.embed_batch_size):
             batch = texts[i:i + self.embed_batch_size]
             payload = {'input': batch if len(batch) > 1 else batch[0]}

             try:
                  response = requests.post(self.endpoint_url, json=payload, headers=self.headers, timeout=30)
                  response.raise_for_status()
                  response_data = response.json()
                  batch_embeddings = [item['embedding'] for item in sorted(response_data['data'], key=lambda x: x['index'])]

                  if len(batch_embeddings) != len(batch):
                       raise ValueError(f"Number of embeddings received ({len(batch_embeddings)}) does not match number of texts sent ({len(batch)})")

                  all_embeddings.extend(batch_embeddings)
                  logger.debug(f"Successfully embedded batch of {len(batch)} texts.")

             except requests.exceptions.Timeout:
                  logger.error(f"Timeout while embedding batch starting with: '{batch[0][:50]}...'")
                  st.error(f"Error: Timeout while generating embeddings for the knowledge base. Try reducing data or check API status.")
                  raise # Re-raise to stop initialization if needed
             except requests.exceptions.RequestException as e:
                  logger.error(f"API request failed while embedding batch: {e}")
                  if e.response is not None:
                      logger.error(f"API Error Response: Status={e.response.status_code}, Body={e.response.text}")
                      st.error(f"API Error ({e.response.status_code}) while generating embeddings. Check API key and endpoint.")
                  else:
                      st.error("Network error while generating embeddings.")
                  raise
             except (KeyError, IndexError, TypeError, ValueError) as e: # Include ValueError
                  logger.error(f"Failed to parse embedding response: {e}. Response data: {response_data}")
                  st.error(f"Invalid response structure from embedding API: {e}")
                  raise ValueError(f"Invalid response structure from embedding API: {e}") from e
             except Exception as e:
                  logger.error(f"An unexpected error occurred during embedding: {e}")
                  st.error(f"An unexpected error occurred during embedding: {e}")
                  raise

        return all_embeddings


    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # ... (Your embed_documents method) ...
        if not texts:
             logger.warning("embed_documents called with empty list.")
             return []
        logger.info(f"Embedding {len(texts)} documents using University API...")
        start_time = time.time()
        embeddings = self._embed(texts)
        end_time = time.time()
        logger.info(f"Finished embedding documents in {end_time - start_time:.2f} seconds.")
        return embeddings


    def embed_query(self, text: str) -> List[float]:
        # ... (Your embed_query method) ...
        if not text:
             logger.warning("embed_query called with empty string.")
             return [] # Return empty list or handle as error?
        logger.info("Embedding query using University API...")
        start_time = time.time()
        query_embedding = self._embed([text])[0]
        end_time = time.time()
        logger.info(f"Finished embedding query in {end_time - start_time:.2f} seconds.")
        return query_embedding

# --- Configuration ---
# *** University API Configuration (Only API Key needed from secrets now) ***
university_api_key = st.secrets.get("university_api_key")
university_base_url = "https://genai.hkbu.edu.hk/general/rest"
university_chat_model_name = "gpt-4-o-mini"
university_embedding_model_name = "text-embedding-3-large" # Still needed for embeddings object
university_api_version = "2024-05-01-preview"
EMBEDDING_BATCH_SIZE = 16

# --- Vector Store Configuration ---
# REMOVED Chroma specific config
# collection_name = "sc_hk_card_info"
# REMOVED ChromaDB Server Config
# chroma_host = st.secrets.get("CHROMA_HOST")
# chroma_port = st.secrets.get("CHROMA_PORT", "8000")

FAISS_INDEX_PATH = "faiss_index" # Path where index files are stored in the repo

# --- Helper function to initialize Vector Store (MODIFIED FOR FAISS) ---
@st.cache_resource(show_spinner="Loading Knowledge Base...")
def initialize_vector_store(_embedding_function):
    logger.info(f"Attempting to load FAISS index from path: {FAISS_INDEX_PATH}")
    vectorstore = None

    if not os.path.exists(FAISS_INDEX_PATH) or \
       not os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.faiss")) or \
       not os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.pkl")):
        error_msg = f"FAISS index files not found in directory '{FAISS_INDEX_PATH}'. " \
                    "Please ensure 'index.faiss' and 'index.pkl' were created and committed to the repository."
        logger.error(error_msg)
        st.error(error_msg)
        st.stop()
        return None

    try:
        vectorstore = FAISS.load_local(
            folder_path=FAISS_INDEX_PATH,
            embeddings=_embedding_function,
            # Deserialization needs to be allowed for loading the .pkl file
            # This is safe if you trust the source of the index files (which you do, as you generated them)
            allow_dangerous_deserialization=True
        )
        logger.info(f"Successfully loaded FAISS index from {FAISS_INDEX_PATH}")
    except Exception as e:
        logger.exception(f"Error loading FAISS index from {FAISS_INDEX_PATH}: {e}")
        st.error(f"Failed to load the Knowledge Base from local files: {e}")
        st.stop()
        return None

    return vectorstore

# --- Streamlit App UI ---
st.set_page_config(page_title="Credit Card FAQ Chatbot", page_icon="💳")
st.title("💳 Standard Chartered HK - Credit Card FAQ")
st.markdown("Using HKBU GenAI Platform API (Chat & Embeddings) | Knowledge Base via FAISS") # Updated description

def clear_chat_history():
    logger.info("Clearing chat history.")
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me about Standard Chartered HK Credit Cards."}]

st.button('Clear Chat History', on_click=clear_chat_history)

# --- Chatbot Logic ---
if not university_api_key:
    st.info("Please add your University API key to Streamlit secrets (key: university_api_key) to continue.", icon="🗝️")
    logger.warning("University API key not found in secrets.")
    st.stop()
else:
    # *** Initialize Custom University Embeddings ***
    try:
        # Embeddings object is needed for loading the FAISS index
        embeddings = UniversityEmbeddings(
            api_key=university_api_key,
            base_url=university_base_url,
            model_name=university_embedding_model_name,
            api_version=university_api_version,
            embed_batch_size=EMBEDDING_BATCH_SIZE
        )
        logger.info(f"University Embeddings client initialized successfully.")
    except Exception as e:
        logger.exception("Failed to initialize University Embeddings client.")
        st.error(f"Failed to initialize University Embeddings service: {e}")
        st.stop()

    # --- Load FAISS Vector Store from local files ---
    vectorstore = initialize_vector_store(embeddings) # Pass embeddings object

    if vectorstore is None:
        logger.error("FAISS vector store loading failed. Stopping execution.")
        # Error message should have been displayed in initialize_vector_store
        st.stop()

    # --- Initialize chat history ---
    if "messages" not in st.session_state:
        logger.info("Initializing chat history session state.")
        st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me anything about Standard Chartered HK Credit Cards."}]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- Handle user input ---
    if prompt := st.chat_input("Ask about cards, fees, offers, services etc..."):
        logger.info(f"User input received: '{prompt}'")
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            thinking_message = st.empty()
            thinking_message.markdown("Thinking... *(Accessing knowledge base & generating response)*")
            with st.spinner("Processing your request..."):
                # --- RAG Step: Retrieve (Now uses FAISS) ---
                context = "Error during context retrieval."
                retrieved_docs_content = []
                try:
                    logger.info(f"Retrieving relevant documents for query: '{prompt}' from FAISS index.")
                    if vectorstore:
                        # The retriever works the same way with FAISS vectorstore object
                        retriever = vectorstore.as_retriever(
                            search_type="similarity",
                            search_kwargs={"k": 10}
                        )
                        # Retriever uses the embed_query method from the embeddings object passed during loading
                        retrieved_docs = retriever.invoke(prompt)
                        retrieved_docs_content = [doc.page_content for doc in retrieved_docs]

                        if not retrieved_docs_content:
                            logger.warning("No relevant documents found in the FAISS knowledge base for the query.")
                            context = "No specific information found in the knowledge base for this query."
                        else:
                            context = "\n\n---\n\n".join(retrieved_docs_content)
                            logger.info(f"Retrieved {len(retrieved_docs)} documents from FAISS index.")
                            logger.debug(f"Retrieved context:\n{context[:500]}...")
                    else:
                         logger.error("Vectorstore object (FAISS) is invalid/None. Cannot retrieve documents.")
                         context = "Error: Failed to access the knowledge base (invalid vectorstore)."

                except Exception as e:
                    logger.exception("Error retrieving documents from FAISS vector store.")
                    st.error(f"Error retrieving information from knowledge base files: {e}")
                    context = "Error: Failed to access the knowledge base files."

                # --- RAG Step: Augment Prompt (No changes needed here) ---
                # ... (system_message_content and messages_for_api remain the same) ...
                system_message_content = """You are an AI assistant for Standard Chartered HK credit cards.
                - Answer the user's question based *ONLY* on the provided context below.
                - Be concise and directly address the question.
                - If the context doesn't contain the answer, state clearly that the information is not available in the provided documents.
                - Do not make up information or use external knowledge.
                - Quote specific fees, rates, or card names from the context when relevant.
                - If the context indicates an error occurred during retrieval, inform the user politely that you couldn't access the necessary information.
                """
                messages_for_api = [
                    {"role": "system", "content": system_message_content},
                    {"role": "user", "content": f"Based on the following information:\n\nContext:\n---\n{context}\n---\n\nQuestion: {prompt}"}
                ]

                # --- RAG Step: Generate (No changes needed here) ---
                # ... (API call logic to University Chat API remains the same) ...
                response_content = "Sorry, I encountered an error processing your request."
                try:
                    url = f"{university_base_url}/deployments/{university_chat_model_name}/chat/completions?api-version={university_api_version}"
                    headers = {
                        'Content-Type': 'application/json',
                        'api-key': university_api_key
                    }
                    payload = { 'messages': messages_for_api }

                    logger.info(f"Sending request to University Chat API: {url}")
                    api_response = requests.post(url, json=payload, headers=headers, timeout=90)
                    api_response.raise_for_status()

                    if api_response.status_code == 200:
                        data = api_response.json()
                        logger.info("Successfully received 200 OK response from University Chat API.")
                        logger.debug(f"Chat API Response Data: {data}")
                        choices = data.get('choices', [])
                        if choices:
                            message = choices[0].get('message', {})
                            content = message.get('content')
                            if content:
                                response_content = content
                                logger.info("Successfully extracted chat response content.")
                            else:
                                logger.error("Could not extract 'content' from chat API response message.")
                                response_content = "Error: Received an incomplete response from the AI chat service."
                        else:
                            logger.error("Could not extract 'choices' from chat API response.")
                            response_content = "Error: Received an invalid response structure from the AI chat service."

                except requests.exceptions.Timeout:
                     logger.error("Request to University Chat API timed out.")
                     st.error("The request to the AI chat service timed out. Please try again.")
                     response_content = "Sorry, the chat request timed out."
                except requests.exceptions.RequestException as e:
                     logger.exception(f"Error calling University Chat API (RequestException): {e}")
                     err_msg = f"An error occurred while communicating with the University AI chat service: {e}"
                     st.error(err_msg)
                     response_content = "Sorry, there was a communication problem with the AI chat service."
                except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e: # Catch parsing/structure errors
                     logger.exception(f"Error parsing/handling response from University Chat API: {e}")
                     st.error("Received an invalid or unexpected response from the University AI chat service.")
                     response_content = "Sorry, the AI chat service sent an unexpected response."
                except Exception as e:
                    logger.exception("An unexpected error occurred during University Chat API interaction.")
                    st.error(f"An unexpected error occurred: {e}")


            thinking_message.empty()
            st.markdown(response_content)
            logger.info(f"Assistant final response displayed.")

        st.session_state.messages.append({"role": "assistant", "content": response_content})

# --- End of App Logic ---