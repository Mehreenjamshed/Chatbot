import streamlit as st
import google.generativeai as genai


# Configure your Gemini API key
GOOGLE_API_KEY = "AIzaSyDTKfybj_UmxxDLo6sgR4m0IZc8PMfUBao"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Ask Mehreen's Chatbot", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Ask Mehreen's Chatbot 💬</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Your AI assistant is here to help you! 🚀</p>", unsafe_allow_html=True)

# Add a text input box for the user to type their query
st.markdown("## ✍️ Enter your query below:")
user_input = st.text_input("", placeholder="Ask me anything...")

# Add some space
st.write("")

# Generate and display the response
if user_input:
    with st.spinner("🤔 Thinking..."):
        output = getResponseFromModel(user_input)
    st.markdown("### 🤖 Chatbot's Response:")
    st.success(output)

# Add a footer with some emojis
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🌟Developed by Mehreen Jamshed🌟</p>", unsafe_allow_html=True)
