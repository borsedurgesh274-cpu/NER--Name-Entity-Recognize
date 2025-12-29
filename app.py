import streamlit as st
import spacy

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Page config
st.set_page_config(
    page_title="NER Dashboard",
    page_icon="🔍",
    layout="centered"
)

# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        Named Entity Recognition (NER)
    </h1>
    <h4 style='text-align: center;'>
        Built using spaCy & Streamlit
    </h4>
    <p style='text-align: center;'>
        Created by <b>Durgesh Borse</b>
