from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import streamlit as st
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# OpenAI
# os.environ['OPEN_API_KEY'] = os.getenv("OPEN_API_KEY")

# Chỉ định đường dẫn cụ thể tới file .env
dotenv_path = "/Users/loinguyen/Documents-not in cloud/Langchain/chatbot/.env"
load_dotenv(dotenv_path=dotenv_path)

# Lấy API Key từ biến môi trường
open_api_key = os.getenv("OPEN_API_KEY")

# Kiểm tra xem API Key đã được load chưa
if open_api_key is None:
    raise ValueError("OPEN_API_KEY not found. Please check your .env file.")

# Đặt API Key vào os.environ nếu cần
os.environ['OPEN_API_KEY'] = open_api_key

print("API Key Loaded:", open_api_key)


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
chain = prompt|RunnablePassthrough()|output_parser   

if input_text:
    st.write(chain.invoke({'question':input_text}))