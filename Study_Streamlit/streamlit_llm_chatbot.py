import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain_openai import ChatOpenAI

template = """\
당신은 상대방의 MBTI를 듣고 그 MBTI에 관한 정보를 알려주는 로봇입니다.
MBTI에 관한 질문에만 답변해주세요.
500자 이내로 상대방의 CHAT에 존댓말로 답변해주세요
"""

session_key = "chat_history"

st.header("MBTI에 대해 알려주는 챗봇")

# 빈 리스트 만들기
if session_key not in st.session_state:
    st.session_state[session_key] = []

# 저장된 체인 불러오기
if "chain" in st.session_state:
    chain = st.session_state["chain"]
    
# 처음에 체인 만들기
else:
    prompt = ChatPromptTemplate.from_messages(
        [("system", template), ("human", "{input}")]
    )
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = prompt | model | StrOutputParser()

# 첫 채팅을 시작할 때 첫 인사 출력
if len(st.session_state[session_key]) == 0:
    greeting = "안녕하세요. 저는 MBTI에 진심인 로봇입니다. 당신의 MBTI는 무엇인가요?"
    st.chat_message("assistant").markdown(greeting)
    st.session_state[session_key].append(
        {"role": "assistant", "content": greeting}
    )

# 채팅 기록이 있을 때 기록된 채팅 출력
else:
    for chat in st.session_state[session_key]:
        st.chat_message(chat["role"]).markdown(chat["content"])

# 입력창
question = st.chat_input(placeholder="메세지 입력")

# 채팅이 입력되었을 때
if question:
    # 입력된 채팅 출력
    st.chat_message("user").markdown(question)
    st.session_state[session_key].append(
        {"role": "user", "content": question}
    )
    answer = chain.invoke({"input": question})
    st.chat_message("assistant").markdown(answer)
    # 답변 출력
    # with st.chat_message("assistant"):
    #     answer = chain.invoke({"input": question})
    #     print(answer)
    st.session_state[session_key].append(
        {"role": "assistant", "content": answer}
    )
