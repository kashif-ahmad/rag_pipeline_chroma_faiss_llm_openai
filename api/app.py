import streamlit as st
import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from fastapi import FastAPI

import uvicorn
from langserve import add_routes

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## create an instance of the API class
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description = "Langchain Server API App"
)

## define our model using llama2
model   = Ollama(model="llama2")
prompt  = ChatPromptTemplate.from_template("Explain in less than 10 words what is {topic}")

## add an API route to be called
add_routes(
    app,
    prompt|model,
    path="/query"
)

## run the api using uvicorn
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)