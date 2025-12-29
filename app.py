import streamlit as st
import spacy
from spacy import displacy

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="NER Dashboard",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Load spaCy Model (Safe for Cloud)
# -----------------------------
@st.cache_resource
def load_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except:
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_nlp()

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center;color:#2E8B57;'>🧠 Named Entity Recognition</h1>
    <p style='text-align:center;font-size:18px;'>
    NLP Dashboard using spaCy & Streamlit
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("⚙️ Controls")
st.sidebar.write("This app extracts named entities such as PERSON, GPE, ORG, etc.")

st.sidebar.markdown(
    """
    **Example Input:**  
    Virat Kohli was born in Delhi and plays cricket for India
    """
)

# -----------------------------
# Main Input Area
# -----------------------------
text = st.text_area(
    "✍️ Enter Text for NER Analysis",
    "Virat Kohli Was Born In Delhi And Playes Cricket For India",
    height=150
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🔍 Run NER Analysis"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        doc = nlp(text)

        col1, col2 = st.columns(2)

        # -----------------------------
        # Entity Table
        # -----------------------------
        with col1:
            st.subheader("📌 Extracted Entities")

            if doc.ents:
                for ent in doc.ents:
                    st.info(f"**Entity:** {ent.text}  \n**Label:** {ent.label_}")
            else:
                st.error("No entities found.")

        # -----------------------------
        # Visual Highlight
        # -----------------------------
        with col2:
            st.subheader("🖍️ Visual Entity Highlighting")
            html = displacy.render(doc, style="ent")
            st.components.v1.html(html, scrolling=True, height=300)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Developed by <b>Durgesh Borse</b> 🚀</p>",
    unsafe_allow_html=True
)
