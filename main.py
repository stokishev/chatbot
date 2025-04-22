import streamlit as st
from openai import OpenAI
import json 
import decimal 

from config import credit_card_fees_and_rates 
from tasks import generate_system_message

# --- Streamlit App UI ---

st.set_page_config(page_title="Credit Card FAQ Chatbot", page_icon="💳")
st.title("💳 Standard Chartered Credit Card FAQ")

# Add a button to clear chat history
def clear_chat_history():
    st.session_state.messages = []

st.button('Clear Chat History', on_click=clear_chat_history)

# --- Chatbot Logic ---

openai_api_key = st.secrets["openai_api_key"]

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field.
    if prompt := st.chat_input("Ask about credit card fees and rates..."):

        # Store and display the user prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate the system message using the function from tasks.py
        system_message_content = generate_system_message()

        # Prepare the messages list for the API call (including the system message).
        messages_for_api = [
            {"role": "system", "content": system_message_content}
        ]
        messages_for_api.extend([
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ])

        # Add a loading indicator while generating the response
        with st.spinner("Getting information..."):
            # Generate a response using the OpenAI API.
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=messages_for_api,
                stream=True,
            )

            # Stream the response to the chat.
            with st.chat_message("assistant"):
                response = st.write_stream(stream)

        # Store the assistant's response in session state.
        st.session_state.messages.append({"role": "assistant", "content": response})

