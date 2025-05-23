from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLM応答関数
def get_response(expert_type, user_input):
    system_msg = f"あなたは{expert_type}の専門家です。質問に的確に答えてください。"
    llm = ChatOpenAI(openai_api_key=api_key, temperature=0)
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    return response.content

# Streamlit UI
st.title("LLM Expert Chat App")
st.write("以下の入力フォームに質問を入力し、専門家の種類を選んでください。")

# ユーザー入力
user_input = st.text_input("質問を入力してください:")

# 専門家タイプ選択
expert_type = st.radio("専門家の種類を選択してください：", ("医療", "金融", "法律", "教育"))

# 回答表示
if st.button("送信"):
    if user_input:
        answer = get_response(expert_type, user_input)
        st.write("### 回答：")
        st.write(answer)
    else:
        st.warning("質問を入力してください。")