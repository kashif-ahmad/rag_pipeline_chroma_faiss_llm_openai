import streamlit as st
import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You can assist with user queries. Please respond to the user questions"),
        ("user","Question:{question}")
    ]
)

## streamlit interface
st.title("Chatbot application with LangChain and Llama2")
input_text = st.text_input("Please enter your question here")

## call Ollama API
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write (chain.invoke ({"question":input_text}))