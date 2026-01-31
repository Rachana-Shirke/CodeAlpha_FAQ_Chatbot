import streamlit as st
import sys

# Allow backend import
sys.path.append("CodeAlpha_FAQ_Chatbot")

from backend.chatbot_engine import FAQChatbot

# Page config
st.set_page_config(
    page_title="Aviation FAQ Chatbot",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Aviation FAQ Chatbot")
st.write("Ask questions related to airports, flights, and aviation services.")

# Load chatbot (cached so it loads once)
@st.cache_resource
def load_chatbot():
    return FAQChatbot("CodeAlpha_FAQ_Chatbot/data/faq_data_clean.csv")

bot = load_chatbot()

# User input
user_question = st.text_input("Enter your question:")

if user_question:
    answer = bot.get_answer(user_question)
    st.success(answer)

st.markdown("---")
st.caption("Built using NLP (TF-IDF + Cosine Similarity)")
