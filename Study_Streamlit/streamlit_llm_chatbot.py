import streamlit as st

# 빈 리스트 만들기
if "messages" not in st.session_state:
    st.session_state["messages"] = []

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
    answer = "즐건 저녁되세요!"
    st.chat_message("assistant").markdown(answer)
    st.session_state["messages"].append({"role":"assistant","content":answer})