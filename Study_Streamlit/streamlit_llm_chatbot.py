import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
template = """\
당신은 상대방의 MBTI를 듣고 그 MBTI에 관한 정보를 알려주는 로봇입니다.
MBTI에 관한 질문에만 답변해주세요.
500자 이내로 상대방의 CHAT에 존댓말로 답변해주세요
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", "{input}")
    ]
)
model = ChatOpenAI(model_name="gpt-3.5-turbo")
chain = prompt | model | StrOutputParser()

container = st.empty()
handler = CustomHandler(container)
answer = self.chain.invoke(
    {"input": question},
    {"callbacks": [handler]}
)
session_key = "chat_history"

# 빈 리스트 만들기
if session_key not in st.session_state:
    st.session_state[session_key] = []

if "chain" in st.session_state:
    chain = st.sessioin_state["chain"]
else:
    
# 첫 채팅을 시작할 때 첫 인사 출력
if len(st.session_state["messages"]) == 0:
    greeting = "안녕하세요. 챗봇입니다."
    st.chat_message("assistant").markdown(greeting)
    st.session_state["messages"].append({"role":"assistant","content":greeting})
# 채팅 기록이 있을 때 기록된 채팅 출력
else:
    for chat in st.session_state["messages"]:
        st.chat_message(chat["role"]).markdown(chat["content"])

# 입력창
question = st.chat_input(placeholder="메세지 입력")

# 채팅이 입력되었을 때
if question:
    # 입력된 채팅 출력
    st.chat_message("user").markdown(question)
    st.session_state["messages"].append({"role":"user", "content":question})
    
    # 답변 출력
    answer = model.invoke(question).content
    st.chat_message("assistant").markdown(answer)
    st.session_state["messages"].append({"role":"assistant","content":answer})

