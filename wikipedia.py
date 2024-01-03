import logging
import os

from dotenv import load_dotenv
from tenacity import retry, wait_random_exponential, stop_after_attempt
import streamlit as st  # Import Streamlit library

import cohere
import weaviate

class SearchEngine:
    WIKIPEDIA_PROPERTIES = ["text", "title", "url", "views", "lang", "_additional { distance score }"]

    def __init__(self, cohere_api_key, weaviate_api_key, weaviate_url):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
        self.cohere = self.__cohere_client(cohere_api_key)
        self.weaviate = self.__weaviate_client(weaviate_api_key, cohere_api_key, weaviate_url)
        logging.info("Initialized SearchEngine with Cohere and Weaviate clients")

    # Other methods remain unchanged

    def __load_environment_vars(self):
        """
        Load environment variables from .env file
        """
        logging.info("Loading environment variables...")

        load_dotenv()
        required_vars = ["COHERE_API_KEY", "WEAVIATE_API_KEY", "WEAVIATE_URL"]
        env_vars = {var: st.text_input(var, os.getenv(var)) for var in required_vars}
        for var, value in env_vars.items():
            if not value:
                raise EnvironmentError(f"{var} environment variable not set.")
        
        logging.info("Environment variables loaded")
        return env_vars

    # Other methods remain unchanged

# Streamlit app
def main():
    st.title("Search Engine Configuration")

    # Collect user inputs for API keys and URL
    cohere_api_key = st.text_input("Enter Cohere API Key:")
    weaviate_api_key = st.text_input("Enter Weaviate API Key:")
    weaviate_url = st.text_input("Enter Weaviate URL:")

    # Create SearchEngine instance with user inputs
    search_engine = SearchEngine(cohere_api_key, weaviate_api_key, weaviate_url)

    # Sidebar with user input values
    st.sidebar.title("User Inputs")
    st.sidebar.write(f"Cohere API Key: {cohere_api_key}")
    st.sidebar.write(f"Weaviate API Key: {weaviate_api_key}")
    st.sidebar.write(f"Weaviate URL: {weaviate_url}")

    # Additional Streamlit app logic
    # ...

if __name__ == "__main__":
    main()

