import streamlit as st
import spacy

# Load model only once
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# Page configuration
st.set_page_config(
    page_title="Deep Learning NER Dashboard",
    page_icon="🧠",
    layout="centered"
)

# Header section
st.markdown("""
<h1 style="text-align:center;color:#2E86C1;">
🧠 Named Entity Recognition Dashboard
</h1>
<h4 style="text-align:center;">
Deep Learning based NLP using spaCy
</h4>
<p style="text-align:center;">
<b>Created by Durgesh Borse</b>
</p>
<hr>
""", unsafe_allow_html=True)

# Input text box
user_text = st.text_area(
    "✍️ Enter text for Entity Extraction:",
    height=160,
    placeholder="Example: Virat Kohli was born in Delhi and plays cricket for India"
)

# Action button
if st.button("🚀 Extract Entities"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        doc = nlp(user_text)

        if doc.ents:
            st.success("✅ Entities Detected")

            for ent in doc.ents:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#ECF0F1;
                        padding:12px;
                        border-left:6px solid #2E86C1;
                        border-radius:8px;
                        margin-bottom:10px;
                    ">
                        <b>Entity:</b> {ent.text} <br>
                        <b>Label:</b> {ent.label_}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("ℹ️ No entities found")

# Sidebar info
st.sidebar.title("📌 About Project")
st.sidebar.info("""
This application uses **spaCy's deep learning NLP model**
to identify named entities such as:

- PERSON  
- LOCATION (GPE)  
- ORGANIZATION  
- DATE  
- NATIONALITY  

Built & Deployed using **Streamlit**
""")

# Footer
st.markdown("""
<hr>
<p style="text-align:center;font-size:12px;">
© 2025 | Deep Learning NLP Project | Durgesh Borse
</p>
""", unsafe_allow_html=True)

