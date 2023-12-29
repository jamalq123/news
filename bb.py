import streamlit as st
from newspaper import Article
from mtranslate import translate

# Your existing code here...

# Replace the translation part of the code with mtranslate
# Translate content if a target language is selected
if target_language != "Original" and target_language is not None:
    if article.text:  # Check if the article text is not empty or None
        translated_title = translate(article.title, target_language)
        translated_text = translate(article.text, target_language)
        translated_summary = translate(article.summary, target_language)

        st.header(f"Translated Content ({target_language})")
        st.subheader("Translated Title")
        st.write(translated_title)
        
        st.subheader("Translated Text")
        st.write(translated_text)
        
        st.subheader("Translated Summary")
        st.write(translated_summary)
    else:
        st.warning("No text available for translation.")
else:
    st.info("Select a target language to translate.")
