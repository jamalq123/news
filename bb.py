import streamlit as st
from newspaper import Article

# Function to extract and display article details
def extract_article_details(article_url):
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()

    st.header("Article Details")
    
    # Display complete text
    st.subheader("Complete Text")
    st.write(article.text)

    # Display keywords
    st.subheader("Keywords")
    st.write(", ".join(article.keywords))

    # Display article summary
    st.header("Article Summary")
    st.subheader(article.title)
    st.write(article.summary)

# Streamlit app
def main():
    st.title("Article Analyzer")

    # Input for article link
    article_link = st.text_input("Enter the article link:")

    if st.button("Analyze"):
        if article_link:
            try:
                extract_article_details(article_link)
            except Exception as e:
                st.error("Error: Unable to analyze the article. Please check the link.")

if __name__ == "__main__":
    main()
