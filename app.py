import streamlit as st
from rag.answer_generator import AnswerGenerator

# Page config
st.set_page_config(
    page_title="Graph-RAG Chatbot",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Graph-RAG Chatbot")
st.caption("Neo4j-powered chatbot with local Mistral LLM")

# Initialize answer generator
@st.cache_resource
def load_answer_generator():
    return AnswerGenerator()

answer_generator = load_answer_generator()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question about the innovation ideas...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = answer_generator.answer(user_input)
            st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
