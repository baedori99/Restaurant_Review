This project is a prototype MBTI chatbot built with Streamlit and OpenAI’s GPT-3.5 API.
It features real-time token streaming, dynamic UI updates, and persistent chat history using session state, aiming to simulate a smooth and friendly user interaction.

# 🤖 MBTI Chatbot with Streamlit & OpenAI

A prototype chatbot that provides MBTI-based feedback using OpenAI's GPT-3.5 model and Streamlit for a lightweight, interactive UI.

---

## 📌 Features

- 💬 Chat interface built with **Streamlit**
- 🧠 Language model powered by **OpenAI GPT-3.5-Turbo**
- ⚙️ **LangChain** integration for modular prompt management
- 🔁 **Streaming response output** using custom token handler
- 💾 Session-based **chat history** tracking

---

## 🧠 How It Works

1. The chatbot starts with a greeting and asks the user’s MBTI.
2. Based on user input, the model responds with relevant MBTI-based personality information.
3. All conversation history is stored using `st.session_state`.
4. A custom `BaseCallbackHandler` displays the LLM output token by token for a real-time feel.

---

## 🛠️ Tech Stack

| Component    | Technology            |
|--------------|------------------------|
| Frontend UI  | Streamlit              |
| LLM Backend  | OpenAI GPT-3.5-Turbo   |
| Prompt Logic | LangChain              |
| State Mgmt   | Streamlit Session State |
| Streaming    | LangChain Callback Handler |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mbti-chatbot.git
cd mbti-chatbot
