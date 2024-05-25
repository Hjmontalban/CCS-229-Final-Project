import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("Hi, I'm Chatbot featuring Gemini-Pro")
# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask me to answer I'm Chatbot...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

# Mental Health Support Section
st.header("Mental Health Support")

# Ask user about their feelings
st.subheader("How do you feel right now?")
user_feeling = st.text_input("I'm feeling...")

# Ask user about their life lately
st.subheader("How is life lately?")
user_life = st.text_area("Life has been...")

# Ask user about the main problem they encounter lately
st.subheader("What is the main problem you encounter lately?")
user_problem = st.text_area("The main problem I'm facing is...")

# Collect responses and provide feedback
if st.button("Submit"):
    # Display user's responses
    st.write("### Your Responses")
    st.write(f"**Feeling:** {user_feeling}")
    st.write(f"**Life lately:** {user_life}")
    st.write(f"**Main problem:** {user_problem}")

    # Provide some feedback or response
    feedback_prompt = f"""
    The user is feeling: {user_feeling}.
    Their life lately has been: {user_life}.
    The main problem they are facing is: {user_problem}.
    """
    feedback_response = st.session_state.chat_session.send_message(feedback_prompt)

    with st.chat_message("assistant"):
        st.markdown(feedback_response.text)
