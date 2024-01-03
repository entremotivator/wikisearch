import streamlit as st
import wikipedia
from dotenv import load_dotenv
import os
import logging
import cohere
import weaviate

# Load environment variables from .env file
load_dotenv()

# -----------------------------------------------------------------------------
# User API Credentials
# -----------------------------------------------------------------------------
st.sidebar.subheader("🔑 User API Credentials")

# Replace 'YOUR_COHERE_API_KEY' and 'YOUR_WEAVIATE_API_KEY' with actual API keys
cohere_api_key = st.text_input("Cohere API Key", key="cohere_api_key", value=os.getenv("YOUR_COHERE_API_KEY"))
weaviate_api_key = st.text_input("Weaviate API Key", key="weaviate_api_key", value=os.getenv("YOUR_WEAVIATE_API_KEY"))

# Replace 'YOUR_WEAVIATE_URL' with actual Weaviate URL
weaviate_url = st.text_input("Weaviate URL", key="weaviate_url", value=os.getenv("YOUR_WEAVIATE_URL"))

# Check if any API key or URL is missing
if not cohere_api_key or not weaviate_api_key or not weaviate_url:
    st.error("Please provide both Cohere and Weaviate API keys, and Weaviate URL.")
    st.stop()

# Initialize Cohere and Weaviate clients
cohere_client = cohere.Client(cohere_api_key)
weaviate_auth_config = weaviate.auth.AuthApiKey(api_key=weaviate_api_key)
weaviate_client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate_auth_config,
    additional_headers={"X-Cohere-Api-Key": cohere_api_key},
)

# -----------------------------------------------------------------------------
# The rest of the Code
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Wikipedia Semantic Search",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Built by @dcarpintero with Cohere and Weaviate"},
)

# Continue with the rest of your code...

# -----------------------------------------------------------------------------
# (Optional) Run Streamlit App
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # ... (Continue with your existing Streamlit code)
