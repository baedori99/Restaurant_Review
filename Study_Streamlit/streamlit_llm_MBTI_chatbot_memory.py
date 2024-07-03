import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain.memory import ConversationBufferMemory
from langchain_core.callbacks import BaseCallbackHandler
from operator import itemgetter
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

template = """\
당신은 상대방의 MBTI를 듣고 그 MBTI에 관한 정보를 알려주는 로봇입니다.
MBTI에 관한 질문에만 답변해주세요.
500자 이내로 상대방의 CHAT에 존댓말로 답변해주세요
"""

session_key = "chat_history"

class CustomHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.container = container
        self.text = ""
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token # 토큰 하나씩 추가
        self.container.markdown(self.text) # 하나씩 추가된 토큰 출력


st.header("MBTI에 대해 알려주는 챗봇")

# 빈 리스트 만들기
if session_key not in st.session_state:
    st.session_state[session_key] = []

# 저장된 체인 불러오기
if "chain" in st.session_state:
    chain = st.session_state["chain"]
    memory = st.session_state["memory"]

# 처음에 체인, 메모리 만들기
else:
    # 대화 버퍼 메모리를 생성하고, 메시지 반환 기능을 활성화
    memory = ConversationBufferMemory(return_messages=True, memory_key = "chat_history")
    runnable = RunnablePassthrough.assign(
        chat_history = RunnableLambda(memory.load_memory_variables)
        | itemgetter("chat_history")
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", template), MessagesPlaceholder(variable_name = "chat_history"), ("human", "{input}")]
    )
    model = ChatOpenAI(model_name="gpt-3.5-turbo", streaming = True)
    chain = runnable | prompt | model | StrOutputParser()
    
    # 체인 및 메모리 저장
    st.session_state["chain"] = chain
    st.session_state["memory"] = memory

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

    # 답변 출력
    with st.chat_message("assistant"):
        container = st.empty()
        handler = CustomHandler(container)
        answer = chain.invoke(
            {"input": question},
            {"callbacks": [handler]}
            )

    st.session_state[session_key].append({"role": "assistant", "content": answer})
    # 메모리 저장
    memory.save_context(
        {"inputs": question},
        {"output": answer}
    )
    
    # 확인용 메모리 출력
    print(memory.load_memory_variables({}))