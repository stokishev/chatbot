# main.py
import streamlit as st
import requests
import json
import os
import shutil
import logging
import time # Added for embedding timing/delays
from typing import List # Added for type hinting in Embeddings class

# --- RAG Libraries ---
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings # Base class for our custom one
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# --- Load Data from Config ---
from config import full_knowledge_text

# --- Logging Configuration ---
log_level = logging.DEBUG
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
log_file = 'chatbot.log'

logging.basicConfig(level=log_level, format=log_format)
logger = logging.getLogger(__name__)


# --- Custom University Embedding Class ---
class UniversityEmbeddings(Embeddings):
    """
    Custom LangChain embedding class for the HKBU GenAI Platform API.
    Assumes the API follows the Azure OpenAI embedding endpoint structure.
    """
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
        # Consider adding batching logic if API supports sending multiple texts per request
        for i in range(0, len(texts), self.embed_batch_size):
             batch = texts[i:i + self.embed_batch_size]
             # Standard Azure OpenAI payload format: {'input': list_of_strings_or_single_string}
             payload = {'input': batch if len(batch) > 1 else batch[0]} # Adjust if API expects single string even in batch

             try:
                  response = requests.post(self.endpoint_url, json=payload, headers=self.headers, timeout=30)
                  response.raise_for_status() # Check for HTTP errors
                  response_data = response.json()

                  # Expected Azure OpenAI response structure:
                  # {'data': [{'embedding': [0.1, ...], 'index': 0}, ...], 'model': '...', 'usage': {...}}
                  # Sort by index to ensure order is maintained if API returns out of order
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
persist_directory = 'sc_hk_card_db'
collection_name = "sc_hk_card_info"
force_recreate_db = True

# --- Helper function to initialize Vector Store ---
@st.cache_resource(show_spinner="Initializing Knowledge Base...")
def initialize_vector_store(text_data, _embedding_function, _persist_directory, _collection_name, _force_recreate=False):
    logger.info(f"Initializing/Loading vector store from: {_persist_directory}")
    vectorstore = None
    if _force_recreate and os.path.exists(_persist_directory):
        logger.warning(f"Force recreating DB. Removing old directory: {_persist_directory}")
        try:
            shutil.rmtree(_persist_directory)
        except OSError as e:
            logger.error(f"Error removing directory {_persist_directory}: {e}")
            st.error(f"Error removing old database directory. Please remove it manually: {_persist_directory}")
            st.stop()


    if os.path.exists(_persist_directory):
        try:
            logger.info(f"Attempting to load existing vector store with {type(_embedding_function)}.") # Log embedding type
            vectorstore = Chroma(
                persist_directory=_persist_directory,
                embedding_function=_embedding_function,
                collection_name=_collection_name
            )
            count = vectorstore._collection.count() # Get count safely
            if count == 0:
                 logger.warning("Vector store exists but is empty. Re-initializing.")
                 vectorstore = None
                 if os.path.exists(_persist_directory): # Clean up empty directory
                    try:
                        shutil.rmtree(_persist_directory)
                    except OSError as e:
                        logger.error(f"Error removing empty directory {_persist_directory}: {e}")

            else:
                 logger.info(f"Successfully loaded vector store with {count} documents.")

        except Exception as e:
            logger.exception(f"Error loading existing vector store: {e}. Will attempt re-initialization.") # Log full traceback
            vectorstore = None
            if os.path.exists(_persist_directory):
                try:
                    shutil.rmtree(_persist_directory)
                except OSError as e:
                     logger.error(f"Error removing potentially corrupted directory {_persist_directory}: {e}")


    if vectorstore is None:
        logger.info(f"Creating new vector store in: {_persist_directory}")
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

            logger.info(f"Creating Chroma store with {type(_embedding_function)}.")
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=_embedding_function,
                persist_directory=_persist_directory,
                collection_name=_collection_name
            )
            # Add a small delay to ensure persistence before counting
            time.sleep(1)
            count = vectorstore._collection.count()
            logger.info(f"Created and persisted new vector store with {count} documents.")
            if count == 0:
                 logger.error("Vector store created but appears empty. Check embedding process and API responses.")
                 st.error("Error: Knowledge base was created but seems empty. Check logs for embedding errors.")
                 st.stop()
                 return None

        except Exception as e:
            logger.exception(f"Fatal error during vector store creation: {e}")
            st.error(f"Fatal error creating knowledge base: {e}")
            st.stop()
            return None

    return vectorstore

# --- Streamlit App UI ---
st.set_page_config(page_title="Credit Card FAQ Chatbot", page_icon="💳")
st.title("💳 Standard Chartered HK - Credit Card FAQ")
st.markdown("Using HKBU GenAI Platform API (Chat & Embeddings)") # Indicate API source

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
    # *** Initialize Custom University Embeddings WITH BATCH SIZE ***
    try:
        embeddings = UniversityEmbeddings(
            api_key=university_api_key,
            base_url=university_base_url,
            model_name=university_embedding_model_name,
            api_version=university_api_version,
            embed_batch_size=EMBEDDING_BATCH_SIZE
        )
        # Log the batch size being used
        logger.info(f"University Embeddings client initialized successfully with batch size {embeddings.embed_batch_size}.")
    except Exception as e:
        logger.exception("Failed to initialize University Embeddings client.")
        st.error(f"Failed to initialize University Embeddings service: {e}")
        st.stop()

    # --- Load or Initialize Vector Store ---
    vectorstore = initialize_vector_store(
        full_knowledge_text,
        embeddings,
        persist_directory,
        collection_name,
        force_recreate_db
    )

    if vectorstore is None:
        logger.error("Vector store initialization failed. Stopping execution.")
        st.error("Failed to initialize the knowledge base. Please check the logs for embedding API errors.")
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
            thinking_message = st.empty() # Placeholder for spinner/message
            thinking_message.markdown("Thinking... *(Please wait, generating full response)*")
            with st.spinner("Processing your request..."):
                # --- RAG Step: Retrieve ---
                context = "Error during context retrieval."
                retrieved_docs_content = []
                try:
                    logger.info(f"Retrieving relevant documents for query: '{prompt}'")
                    retriever = vectorstore.as_retriever(
                        search_type="similarity",
                        search_kwargs={"k": 10}
                    )
                    retrieved_docs = retriever.invoke(prompt) # Uses embed_query
                    retrieved_docs_content = [doc.page_content for doc in retrieved_docs]

                    if not retrieved_docs_content:
                         logger.warning("No relevant documents found in the knowledge base for the query.")
                         context = "No specific information found in the knowledge base for this query."
                    else:
                        context = "\n\n---\n\n".join(retrieved_docs_content)
                        logger.info(f"Retrieved {len(retrieved_docs)} documents.")
                        logger.debug(f"Retrieved context:\n{context[:500]}...")

                except Exception as e:
                    logger.exception("Error retrieving documents from vector store.")
                    st.error(f"Error retrieving information from knowledge base: {e}")
                    context = "Error: Failed to access the knowledge base."

                # --- RAG Step: Augment Prompt ---
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

                # --- RAG Step: Generate ---
                response_content = "Sorry, I encountered an error processing your request."
                try:
                    url = f"{university_base_url}/deployments/{university_chat_model_name}/chat/completions?api-version={university_api_version}"
                    headers = {
                        'Content-Type': 'application/json',
                        'api-key': university_api_key
                    }
                    payload = { 'messages': messages_for_api }

                    logger.info(f"Sending request to University Chat API: {url}")
                    api_response = requests.post(url, json=payload, headers=headers, timeout=90) # Increased timeout for chat potentially
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