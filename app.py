import streamlit as st
import wikipedia
from dotenv import load_dotenv
import os
import logging
from tenacity import retry, wait_random_exponential, stop_after_attempt
import cohere
import weaviate

# Load environment variables from .env file
load_dotenv()

# -----------------------------------------------------------------------------
# User API Credentials
# -----------------------------------------------------------------------------
st.sidebar.subheader("🔑 User API Credentials")

# Replace 'YOUR_COHERE_API_KEY' and 'YOUR_WEAVIATE_API_KEY' with actual API keys
cohere_api_key = st.sidebar.text_input("Cohere API Key", key="cohere_api_key", value=os.getenv("YOUR_COHERE_API_KEY"))
weaviate_api_key = st.sidebar.text_input("Weaviate API Key", key="weaviate_api_key", value=os.getenv("YOUR_WEAVIATE_API_KEY"))

# Replace 'YOUR_WEAVIATE_URL' with actual Weaviate URL
weaviate_url = st.sidebar.text_input("Weaviate URL", key="weaviate_url", value=os.getenv("YOUR_WEAVIATE_URL"))

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


@st.cache_resource(show_spinner=False)
def load_semantic_engine():
    try:
        return wikipedia.SearchEngine()
    except (OSError, EnvironmentError) as e:
        st.error(f'Semantic Engine Error {e}')
        st.stop()


wikisearch = load_semantic_engine()

@st.cache_data
def query_bm25(query, lang='en', top_n=10):
    try:
        return wikisearch.with_bm25(query, lang=lang, top_n=top_n)
    except (Exception) as e:
        st.error(f'Querying Engine Error {e}')

# Continue with the rest of your existing code...

# -----------------------------------------------------------------------------
# (Optional) Run Streamlit App
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # ... (Continue with your existing Streamlit code)
