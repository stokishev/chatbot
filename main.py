# main.py
import streamlit as st
from openai import OpenAI
import json
import decimal
import os
import shutil
import logging # <-- Import logging module

# --- RAG Libraries ---
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# --- Load Data from Config ---
from config import full_knowledge_text # (Ensure other necessary imports from config are present if needed)

# --- Logging Configuration ---
log_level = logging.DEBUG
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
log_file = 'chatbot.log' # Optional: File to log to

logging.basicConfig(level=log_level, format=log_format)

# Get a logger instance for this module
logger = logging.getLogger(__name__)

# --- Configuration ---
openai_api_key = st.secrets.get("openai_api_key") # Use .get for safer access
persist_directory = 'sc_hk_card_db'
collection_name = "sc_hk_card_info"
force_recreate_db = True

# --- Helper function to initialize Vector Store ---
@st.cache_resource(show_spinner="Initializing Knowledge Base...")
def initialize_vector_store(text_data, _embedding_function, _persist_directory, _collection_name, _force_recreate=False):
    """Initializes or loads the Chroma vector store."""
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
            logger.info(f"Attempting to load existing vector store.")
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

            # Create and persist the vector store
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=_embedding_function,
                persist_directory=_persist_directory,
                collection_name=_collection_name
            )
            logger.info(f"Created and persisted new vector store with {vectorstore._collection.count()} documents.")

        except Exception as e:
            logger.exception(f"Fatal error during vector store creation: {e}") 
            st.error(f"Fatal error creating knowledge base: {e}")
            st.stop()
            return None

    return vectorstore

# --- Streamlit App UI ---
st.set_page_config(page_title="Credit Card FAQ Chatbot", page_icon="💳")
st.title("💳 Standard Chartered HK - Credit Card FAQ")

def clear_chat_history():
    logger.info("Clearing chat history.")
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me about Standard Chartered HK Credit Card features, fees, offers, or services."}]
    

st.button('Clear Chat History', on_click=clear_chat_history)

# --- Chatbot Logic ---
if not openai_api_key:
    st.info("Please add your OpenAI API key to Streamlit secrets (key: openai_api_key) to continue.", icon="🗝️")
    logger.warning("OpenAI API key not found in secrets.")
    st.stop()
else:
    # Initialize OpenAI client and embeddings
    try:
        client = OpenAI(api_key=openai_api_key)
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, model="text-embedding-3-small")
        logger.info("OpenAI client and embeddings initialized successfully.")
    except Exception as e:
        logger.exception("Failed to initialize OpenAI Client or Embeddings.") 
        st.error(f"Failed to initialize OpenAI services: {e}")
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
        st.stop()

    # --- Initialize chat history ---
    if "messages" not in st.session_state:
        logger.info("Initializing chat history session state.")
        st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me about Standard Chartered HK Credit Card features, fees, offers, or services."}]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- Handle user input ---
    if prompt := st.chat_input("Ask about cards, fees, offers or services..."):
        logger.info(f"User input received: '{prompt}'")
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Add a thinking indicator
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # --- RAG Step: Retrieve ---
                context = "Error during context retrieval." 
                retrieved_docs_content = [] # To store content for logging
                try:
                    logger.info(f"Retrieving relevant documents for query: '{prompt}'")
                    retriever = vectorstore.as_retriever(
                        search_type="similarity",
                        search_kwargs={"k": 10} 
                    )
                    # retriever = vectorstore.as_retriever(
                    # search_type="mmr",
                    # search_kwargs={"k": 5, "fetch_k": 20} # Fetch 20 initially, pick top 5 diverse ones
                    # )
                    retrieved_docs = retriever.invoke(prompt)
                    retrieved_docs_content = [doc.page_content for doc in retrieved_docs]
                    context = "\n\n---\n\n".join(retrieved_docs_content)
                    logger.info(f"Retrieved {len(retrieved_docs)} documents.")
                    logger.debug(f"Retrieved context:\n{context}")

                except Exception as e:
                    logger.exception("Error retrieving documents from vector store.") 
                    st.error(f"Error retrieving information from knowledge base: {e}")

                # --- RAG Step: Augment Prompt ---
                system_message_content = """You are an AI assistant for Standard Chartered HK credit cards.
                - Answer the user's question based *ONLY* on the provided context below.
                - Be concise and directly address the question.
                - If the context doesn't contain the answer, state clearly that the information is not available in the provided documents.
                - Do not make up information or use external knowledge.
                - Quote specific fees, rates, or card names from the context when relevant.
                """

                messages_for_api = [
                    {"role": "system", "content": system_message_content},
                    {"role": "user", "content": f"Based on the following information:\n\nContext:\n---\n{context}\n---\n\nQuestion: {prompt}"}
                ]
                logger.debug(f"Messages prepared for OpenAI API: {messages_for_api}")
                logger.info("Sending request to OpenAI API.")


                # --- RAG Step: Generate ---
                response = "Sorry, I encountered an error processing your request." 
                try:
                    stream = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=messages_for_api,
                        stream=True,
                        temperature=0.2,
                        max_tokens=500
                    )
                    # Stream response to the chat
                    response = st.write_stream(stream)
                    logger.info("Successfully received stream response from OpenAI.")
                    logger.debug(f"LLM Response: {response}")


                except Exception as e:
                    logger.exception("Error calling OpenAI API.") 
                    st.error(f"An error occurred while communicating with the AI: {e}")
                    # Keep default error response

            # Add assistant response (or error message) to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            if 'stream' not in locals(): # If API call failed before stream started
                 logger.warning(f"Assistant final response (error default): {response}")


# --- End of App Logic ---