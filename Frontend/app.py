import os
import sys
import streamlit as st

# Add backend directory to python path so we can import query_rag_system
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))
)
from main import query_rag_system

# Page Configuration
st.set_page_config(
    page_title="GAFI Egypt | Business & Legal RAG Advisor",
    page_icon="🇪🇬",
    layout="centered",
)

# --- GAFI Custom Theme Styling ---
st.markdown(
    """
    <style>
    /* Main background color */
    .stApp {
        background: linear-gradient(180deg, #0b1526 0%, #11223a 100%);
        color: #f8fafc;
    }

    /* General text readability */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"] {
        color: #f8fafc !important;
    }

    /* Title and headers */
    h1, h2, h3 {
        color: #f3c654 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Captions and text */
    p, li, label, .stCaption, .stMarkdown {
        color: #f8fafc !important;
    }

    /* Better contrast for markdown text */
    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown ul,
    .stMarkdown ol,
    .stMarkdown strong,
    .stMarkdown em,
    .stMarkdown a {
        color: #f8fafc !important;
        line-height: 1.6;
    }

    .stMarkdown a {
        color: #7cc7ff !important;
        text-decoration: underline;
    }

    /* Deep override for Streamlit chat input box text color */
    div[data-baseweb="base-input"], div[data-baseweb="input"] {
        background-color: #ffffff !important;
    }

    .stChatInput textarea {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Chat message visibility */
    [data-testid="stChatMessage"] {
        background-color: #172c47 !important;
        border: 1px solid #2f4d73 !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        margin: 8px 0 !important;
        box-shadow: none !important;
    }

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] ul,
    [data-testid="stChatMessage"] ol,
    [data-testid="stChatMessage"] strong,
    [data-testid="stChatMessage"] em,
    [data-testid="stChatMessage"] a {
        color: #f8fafc !important;
        line-height: 1.6;
        font-size: 1.02rem;
    }

    [data-testid="stChatMessage"] a {
        color: #8ed0ff !important;
    }

    /* User message bubble */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1d3458 !important;
        border-color: #3a5d8a !important;
    }

    /* Assistant message bubble */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: #13263d !important;
        border-color: #f3c654 !important;
    }

    /* Accent highlights */
    .highlight {
        color: #f3c654;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.title("🇪🇬 GAFI Egypt Business & Legal Assistant")
st.markdown(
    "Official guidance portal for <span class='highlight'>Law 159/1981</span>,"
    " <span class='highlight'>MSME Law 152/2020</span>, company incorporation"
    " steps, and venture capital directory.",
    unsafe_allow_html=True,
)
st.divider()

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display prior chat messages from history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Accept user input from chat box
if prompt := st.chat_input(
    "Ask about GAFI company setup, legal articles, or funding sources..."
):
  # Add user message to session state and display it
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Generate assistant response using your backend RAG function
  with st.chat_message("assistant"):
    with st.spinner("Searching official Egyptian regulations..."):
      response = query_rag_system(prompt)
    st.markdown(response)

  # Add assistant response to session state
  st.session_state.messages.append({"role": "assistant", "content": response})