import streamlit as st
import google.generativeai as genai

st.title("Welcome to Gemini Chat")

genai.configure(api_key="AIzaSyBdoGj03i_gZwZNRdMhwnjJyTJeBOpb8mI")

text = st.text_input ("Ask Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me to get answer"):
    response = chat.send_message(text)
    st.write(response.text)
