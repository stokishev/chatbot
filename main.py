# main.py
import sys
import streamlit as st
import requests
import json
import os
# import shutil # No longer needed for directory management
import logging
import time
from typing import List

# --- RAG Libraries ---
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import chromadb # Import the chromadb client library
from chromadb.config import Settings # For client settings if needed
# from chromadb.errors import CollectionNotFoundError # Specific error for checking collection existence

# --- Load Data from Config ---
from config import full_knowledge_text

# --- Logging Configuration ---
log_level = logging.DEBUG
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
log_file = 'chatbot.log' # Log file might be less useful in ephemeral environments like Streamlit Cloud

logging.basicConfig(level=log_level, format=log_format, stream=sys.stdout) # Log to stdout for cloud environments
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
        embed_batch_size: int = 1 # Process texts one by one by default
    ):
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
        """Internal method to handle embedding requests."""
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
                  # Optional: Add a small delay if hitting rate limits
                  # if len(texts) > 10: time.sleep(0.05)

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
        """Embed a list of documents."""
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
        """Embed a single query."""
        if not text:
             logger.warning("embed_query called with empty string.")
             return [] # Return empty list or handle as error?
        logger.info("Embedding query using University API...")
        start_time = time.time()
        query_embedding = self._embed([text])[0]
        end_time = time.time()
        logger.info(f"Finished embedding query in {end_time - start_time:.2f} seconds.")
        return query_embedding
# --- End of Custom University Embedding Class ---


# --- Configuration ---
# *** University API Configuration ***
university_api_key = st.secrets.get("university_api_key")
university_base_url = "https://genai.hkbu.edu.hk/general/rest"
university_chat_model_name = "gpt-4-o-mini" # Model for chat
university_embedding_model_name = "text-embedding-3-large"
university_api_version = "2024-05-01-preview"
EMBEDDING_BATCH_SIZE = 16

# --- Vector Store Configuration ---
# persist_directory = 'sc_hk_card_db' # REMOVED: No longer persisting locally
collection_name = "sc_hk_card_info"
force_recreate_db = True # Be careful with this in production!

# *** ChromaDB Server Configuration (Fetch from Secrets) ***
chroma_host = st.secrets.get("CHROMA_HOST")
chroma_port = st.secrets.get("CHROMA_PORT", "8000") # Default Chroma port is 8000

# --- Helper function to initialize Vector Store (MODIFIED for alternative error handling) ---
@st.cache_resource(show_spinner="Connecting to Knowledge Base...")
def initialize_vector_store(text_data, _embedding_function, _collection_name, _chroma_host, _chroma_port, _force_recreate=False):
    logger.info(f"Attempting to connect to ChromaDB server at {_chroma_host}:{_chroma_port}")
    vectorstore = None
    chroma_client = None

    if not _chroma_host:
        st.error("ChromaDB host address is not configured in Streamlit secrets (key: CHROMA_HOST).")
        logger.error("CHROMA_HOST secret not found.")
        st.stop()
        return None

    try:
        chroma_client = chromadb.HttpClient(
            host=_chroma_host,
            port=_chroma_port,
            settings=Settings(allow_reset=True, anonymized_telemetry=False)
        )
        chroma_client.heartbeat()
        logger.info("Successfully connected to ChromaDB server.")

    except Exception as e:
        logger.exception(f"Failed to connect to ChromaDB server at {_chroma_host}:{_chroma_port}: {e}")
        st.error(f"Error connecting to the Knowledge Base server ({_chroma_host}:{_chroma_port}). Please ensure it's running and accessible.")
        st.stop()
        return None

    collection_exists = False
    try:
        # *** MODIFICATION START ***
        # Check using list_collections instead of relying on get_collection's exception
        existing_collections = chroma_client.list_collections()
        collection_names = [col.name for col in existing_collections]

        if _collection_name in collection_names:
            logger.info(f"Collection '{_collection_name}' found in list on ChromaDB server.")
            collection_exists = True
        else:
            logger.info(f"Collection '{_collection_name}' not found in list on ChromaDB server.")
            collection_exists = False
        # *** MODIFICATION END ***

    except Exception as e:
        # Handle potential errors during list_collections itself
        logger.exception(f"Error checking for collection '{_collection_name}' via list_collections: {e}")
        st.error(f"Error accessing Knowledge Base collection list '{_collection_name}'.")
        collection_exists = False # Assume it doesn't exist or is inaccessible if error

    # --- Force recreate logic remains the same ---
    if _force_recreate and collection_exists:
        logger.warning(f"Force recreating DB. Deleting existing collection: {_collection_name}")
        try:
            chroma_client.delete_collection(name=_collection_name)
            logger.info(f"Successfully deleted collection: {_collection_name}")
            collection_exists = False
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error deleting collection {_collection_name}: {e}")
            st.error(f"Error deleting existing Knowledge Base collection '{_collection_name}'. Please check ChromaDB server logs.")
            st.stop()
            return None

    # --- Loading/Creation logic remains the same, relying on the collection_exists flag ---
    if collection_exists:
        try:
            logger.info(f"Attempting to load existing vector store '{_collection_name}' using Langchain Chroma client.")
            vectorstore = Chroma(
                client=chroma_client,
                collection_name=_collection_name,
                embedding_function=_embedding_function,
            )
            count = vectorstore._collection.count()
            if count == 0:
                logger.warning(f"Remote vector store '{_collection_name}' exists but is empty. Re-initializing.")
                collection_exists = False
                try:
                    chroma_client.delete_collection(name=_collection_name)
                    logger.info(f"Deleted empty collection '{_collection_name}'.")
                except Exception as e_del:
                    logger.error(f"Failed to delete empty collection '{_collection_name}': {e_del}")
            else:
                logger.info(f"Successfully loaded vector store '{_collection_name}' with {count} documents from ChromaDB server.")
        except Exception as e:
            logger.exception(f"Error loading existing vector store '{_collection_name}' from client: {e}. Will attempt re-initialization if possible.")
            st.warning(f"Could not load existing knowledge base '{_collection_name}'. Attempting to create a new one.")
            vectorstore = None
            collection_exists = False

    if not collection_exists:
        # ... (rest of the creation logic using Chroma.from_documents) ...
        logger.info(f"Creating new vector store collection: {_collection_name} on ChromaDB server.")
        if not text_data:
            logger.error("Source text data is empty. Cannot initialize vector store.")
            st.error("Error: The source knowledge text is empty. Cannot build the knowledge base.")
            st.stop()
            return None

        docs = [Document(page_content=text_data)]
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len,
        )
        try:
            chunks = text_splitter.split_documents(docs)
            logger.info(f"Split data into {len(chunks)} chunks.")

            if not chunks:
                logger.error("No chunks were created from the source data.")
                st.error("Error: No text chunks could be created from the source data.")
                st.stop()
                return None

            logger.info(f"Creating Chroma collection '{_collection_name}' via Langchain with {type(_embedding_function)}.")
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=_embedding_function,
                collection_name=_collection_name,
                client=chroma_client,
            )
            time.sleep(2)
            count = vectorstore._collection.count()
            logger.info(f"Created and populated collection '{_collection_name}' with {count} documents on ChromaDB server.")
            if count == 0:
                logger.error("Vector store collection created but appears empty. Check embedding process and API responses.")
                st.error("Error: Knowledge base was created but seems empty. Check logs for embedding errors.")
                st.stop()
                return None

        except Exception as e:
            logger.exception(f"Fatal error during vector store creation on ChromaDB server: {e}")
            st.error(f"Fatal error creating knowledge base on ChromaDB server: {e}")
            st.stop()
            return None

    return vectorstore

# --- Streamlit App UI ---
st.set_page_config(page_title="Credit Card FAQ Chatbot", page_icon="💳")
st.title("💳 Standard Chartered HK - Credit Card FAQ")
st.markdown("Using HKBU GenAI Platform API (Chat & Embeddings) | Knowledge Base via ChromaDB Server") # Updated description

def clear_chat_history():
    logger.info("Clearing chat history.")
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me about Standard Chartered HK Credit Cards."}]

st.button('Clear Chat History', on_click=clear_chat_history)

# --- Chatbot Logic ---
if not university_api_key:
    st.info("Please add your University API key to Streamlit secrets (key: university_api_key) to continue.", icon="🗝️")
    logger.warning("University API key not found in secrets.")
    st.stop()
elif not chroma_host:
    # Error message already handled in initialize_vector_store if secret is missing
    # st.info("Please add your ChromaDB server host to Streamlit secrets (key: CHROMA_HOST).", icon="☁️")
    logger.warning("ChromaDB host not found in secrets.")
    st.stop() # Stop here if Chroma host is missing
else:
    # *** Initialize Custom University Embeddings ***
    try:
        embeddings = UniversityEmbeddings(
            api_key=university_api_key,
            base_url=university_base_url,
            model_name=university_embedding_model_name,
            api_version=university_api_version,
            embed_batch_size=EMBEDDING_BATCH_SIZE
        )
        logger.info(f"University Embeddings client initialized successfully with batch size {embeddings.embed_batch_size}.")
    except Exception as e:
        logger.exception("Failed to initialize University Embeddings client.")
        st.error(f"Failed to initialize University Embeddings service: {e}")
        st.stop()

    # --- Connect to or Initialize Vector Store on ChromaDB Server ---
    vectorstore = initialize_vector_store(
        full_knowledge_text,
        embeddings, # Pass the initialized embedding function
        collection_name,
        chroma_host,
        chroma_port,
        force_recreate_db # Pass the flag
    )

    if vectorstore is None:
        # Errors should be handled within initialize_vector_store, but double-check
        logger.error("Vector store initialization failed. Stopping execution.")
        if not st.secrets.get("CHROMA_HOST"):
             st.error("Knowledge base connection failed: ChromaDB host not configured in secrets.")
        else:
             st.error("Failed to initialize/connect to the knowledge base. Please check the logs and ensure the ChromaDB server is running and accessible.")
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

        # Add a thinking indicator
        with st.chat_message("assistant"):
            thinking_message = st.empty()
            thinking_message.markdown("Thinking... *(Accessing knowledge base & generating response)*")
            with st.spinner("Processing your request..."):
                # --- RAG Step: Retrieve ---
                context = "Error during context retrieval."
                retrieved_docs_content = []
                try:
                    logger.info(f"Retrieving relevant documents for query: '{prompt}' from ChromaDB server.")
                    # Ensure the vectorstore object is valid before creating retriever
                    if vectorstore:
                        retriever = vectorstore.as_retriever(
                            search_type="similarity",
                            search_kwargs={"k": 10} # Retrieve top 10 docs
                        )
                        # The retriever uses the embedding function associated with the vectorstore
                        retrieved_docs = retriever.invoke(prompt)
                        retrieved_docs_content = [doc.page_content for doc in retrieved_docs]

                        if not retrieved_docs_content:
                            logger.warning("No relevant documents found in the remote knowledge base for the query.")
                            context = "No specific information found in the knowledge base for this query."
                        else:
                            context = "\n\n---\n\n".join(retrieved_docs_content)
                            logger.info(f"Retrieved {len(retrieved_docs)} documents from ChromaDB server.")
                            logger.debug(f"Retrieved context:\n{context[:500]}...")
                    else:
                         logger.error("Vectorstore object is invalid/None. Cannot retrieve documents.")
                         context = "Error: Failed to access the knowledge base (invalid vectorstore)."


                except Exception as e:
                    logger.exception("Error retrieving documents from vector store client.")
                    st.error(f"Error retrieving information from knowledge base server: {e}")
                    context = "Error: Failed to access the knowledge base server."

                # --- RAG Step: Augment Prompt (No changes needed here) ---
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
                logger.debug(f"Messages prepared for University Chat API: {messages_for_api}")

                # --- RAG Step: Generate (No changes needed here) ---
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

            # *** Clear the 'Thinking...' message and display the final response ***
            thinking_message.empty() # Remove the spinner/message
            st.markdown(response_content) # Display the complete response
            logger.info(f"Assistant final response displayed.")


        # Add assistant response (or error message) to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content})

# --- End of App Logic ---