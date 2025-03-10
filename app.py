from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# OpenAI
os.environ['OPEN_API_KEY'] = os.getenv("OPEN_API_KEY")


## Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "you are a helpful assistant. Please response to the user queries."),
        ('user', "Question: {question}")
    ]
)

##streamlit framework

st.title("Langchain Demo with Open API")
input_text = st.text_input("Search the topic u want")

# openAI llm

llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|input_text|output_parser   

if input_text:
    st.write(chain.invoke({'Question':input_text}))