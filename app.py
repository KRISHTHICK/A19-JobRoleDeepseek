import streamlit as st
import subprocess

st.set_page_config(page_title="💼 Job Role Advisor (Local)", layout="wide")
st.title("🤖💬 Local Job Role Advisor Chatbot (DeepSeek + Ollama)")

st.markdown("""
Ask me about any **job role**, **career path**, or **required skills**.
Examples:
- What does a cloud engineer do?
- Skills needed for data scientist
- How to become a machine learning engineer?
""")

# Store conversation in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from user
user_input = st.chat_input("Ask me about jobs, skills, or roles...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking with DeepSeek..."):
        # Format the prompt
        prompt = f"You are a helpful job and career advisor. Answer the following:\n{user_input}"

        # Run local DeepSeek model via Ollama
        result = subprocess.run(
            ["ollama", "run", "deepseek-coder", prompt],
            capture_output=True,
            text=True
        )

        # Get model response
        response = result.stdout.strip()

    # Display and store response
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
