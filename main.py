import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


load_dotenv()


st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


st.title("Hi, I'm Chatbot for Mental Support featuring Gemini-Pro")
# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


user_prompt = st.chat_input("Ask me to answer I'm Chatbot...")
if user_prompt:

    st.chat_message("user").markdown(user_prompt)

 
    gemini_response = st.session_state.chat_session.send_message(user_prompt)


    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

st.header("🩺Mental Health Support")


st.subheader("How do you feel right now?")
user_feeling = st.text_input("I'm feeling...")

st.subheader("How is life lately?")
user_life = st.text_area("Life has been...")


st.subheader("What is the main problem you encounter lately?")
user_problem = st.text_area("The main problem I'm facing is...")

if st.button("Submit"):

    st.write("### Your Responses")
    st.write(f"**Feeling:** {user_feeling}")
    st.write(f"**Life lately:** {user_life}")
    st.write(f"**Main problem:** {user_problem}")

    feedback_prompt = f"""
    The user is feeling: {user_feeling}.
    Their life lately has been: {user_life}.
    The main problem they are facing is: {user_problem}.
    """
    feedback_response = st.session_state.chat_session.send_message(feedback_prompt)

    with st.chat_message("assistant"):
        st.markdown(feedback_response.text)
