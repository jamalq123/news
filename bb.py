import streamlit as st
from newspaper import Article
from googletrans import Translator
import nltk
import os

# Download 'punkt' tokenizer if not already downloaded
nltk.download('punkt', quiet=True)

# Function to set NLTK data path using Streamlit environment variables
def set_nltk_data_path():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    nltk.data.path.append(os.path.join(st.__path__[0], 'nltk_data'))

# Function to extract and display article details
def extract_article_details(article_url, target_language):
    set_nltk_data_path()  # Set NLTK data path

    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()
    translator = Translator()
    
    st.header("Article Details")
    
    # Rest of your code for displaying article details and translation...

# Streamlit app
def main():
    st.title("Article Translator")

    article_link = st.text_input("Enter the URL of the article:")
    target_language = st.selectbox("Select a target language:", ["Original", "Spanish", "French", "German", "Italian", "Urdu"])

    if st.button("Translate"):
        if article_link:
            try:
                extract_article_details(article_link, target_language)
            except Exception as e:
                st.error(f"Error: Unable to analyze the article. Please check the link. Exception: {e}")
                st.exception(e)

if __name__ == "__main__":
    main()
