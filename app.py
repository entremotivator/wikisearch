import streamlit as st
import wikipedia

st.set_page_config(
    page_title="Wikipedia Semantic Search",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Built by @dcarpintero with Cohere and Weaviate"},
)

class SearchEngine:
    WIKIPEDIA_PROPERTIES = ["text", "title", "url", "views", "lang", "_additional { distance score }"]

    def __init__(self):
        self.cohere_api_key = None
        self.weaviate_api_key = None
        self.weaviate_url = None
        self.cohere = None
        self.weaviate = None
        self.load_api_credentials()
        self.initialize_clients()

    def load_api_credentials(self):
        """
        Load API credentials from user input or environment variables
        """
        st.title("Search Engine Configuration")

        # Collect user inputs for API keys and URL
        self.cohere_api_key = st.text_input("Enter Cohere API Key:")
        self.weaviate_api_key = st.text_input("Enter Weaviate API Key:")
        self.weaviate_url = st.text_input("Enter Weaviate URL:")

        # Sidebar with user input values
        st.sidebar.title("User Inputs")
        st.sidebar.write(f"Cohere API Key: {self.cohere_api_key}")
        st.sidebar.write(f"Weaviate API Key: {self.weaviate_api_key}")
        st.sidebar.write(f"Weaviate URL: {self.weaviate_url}")

    def initialize_clients(self):
        """
        Initialize Cohere and Weaviate clients
        """
        if not self.cohere_api_key or not self.weaviate_api_key or not self.weaviate_url:
            st.warning("⚠️ API keys and URL are required.")
            st.stop()

        try:
            self.cohere = cohere.Client(api_key=self.cohere_api_key)
            self.weaviate = weaviate.Client(
                url=self.weaviate_url, api_key=self.weaviate_api_key)
            logging.info("Initialized SearchEngine with Cohere and Weaviate clients")
        except Exception as e:
            st.error(f"Error initializing clients: {e}")
            st.stop()

    # Other methods remain unchanged

# The rest of your Streamlit app remains the same

# Streamlit app
def main():
    search_engine = SearchEngine()

    # Your existing Streamlit app logic

if __name__ == "__main__":
    main()
