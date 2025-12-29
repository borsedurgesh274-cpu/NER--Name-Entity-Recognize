import streamlit as st
import spacy
from spacy import displacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Page Configuration
st.set_page_config(
    page_title="NER Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Title Section
st.markdown(
    "<h1 style='text-align:center;color:#4CAF50;'>🧠 Named Entity Recognition Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Built using <b>spaCy</b> & <b>Streamlit</b></p>",
    unsafe_allow_html=True
)

st.divider()

# Sidebar
st.sidebar.header("⚙️ App Settings")
st.sidebar.info("Enter any sentence to detect named entities like PERSON, ORG, GPE, etc.")

# Text Input
text = st.text_area(
    "✍️ Enter your text here:",
    "Virat Kohli was born in Delhi and plays cricket for India",
    height=150
)

# Button
if st.button("🔍 Analyze Text"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        doc = nlp(text)

        st.subheader("📌 Extracted Entities")

        if doc.ents:
            for ent in doc.ents:
                st.success(f"**Entity:** {ent.text}  |  **Label:** {ent.label_}")
        else:
            st.error("No entities found.")

        st.divider()

        # Visual NER
        st.subheader("🖼️ Visual Entity Highlighting")
        html = displacy.render(doc, style="ent")
        st.components.v1.html(html, scrolling=True, height=300)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Developed by <b>Durgesh Borse</b> 🚀</p>",
    unsafe_allow_html=True
)
