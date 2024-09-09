import requests
import streamlit as st

def get_llama2_response(input_text):

    response = requests.post(
        "http://localhost:8000/query/invoke",
        json={'input':{'topic':input_text}}
    )

    return response.json()['output']

st.title ('Langchain Demo With Llama2 API')
input_text = st.text_input ("Please explain")

if input_text:
    st.write (get_llama2_response (input_text))