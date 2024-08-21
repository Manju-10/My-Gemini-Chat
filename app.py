import streamlit as st
import google.generativeai as genai

# Set custom title with HTML/CSS for blue glow effect on both text and icon
st.markdown(
    """
    <h1 style="text-align: center; color: #00BFFF; font-size: 50px;
    text-shadow: 0 0 10px #00BFFF;
    filter: brightness(1.5);">
    <img src="https://icon-library.com/images/ai-icon/ai-icon-7.jpg" alt="icon" 
    style="width:50px;height:50px;vertical-align:middle;margin-right:10px;
    filter: brightness(2);">
    Welcome to Gemini Chat
    </h1>
    """,
    unsafe_allow_html=True
)

# Configuration for the Google Generative AI
genai.configure(api_key="AIzaSyBdoGj03i_gZwZNRdMhwnjJyTJeBOpb8mI")

# User input
text = st.text_input("Ask Your Question")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Button to get the answer
if st.button("Click me to get answer"):
    response = chat.send_message(text)
    st.write(response.text)
