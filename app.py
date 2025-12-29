import streamlit as st
import spacy
from spacy import displacy

# Load the model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Dashboard Title
st.title("🏷️ Entity Extraction Dashboard")
st.markdown("Enter text below to identify names, locations, and organizations.")

# User input
text_input = st.text_area("Input Text:", "Virat Kohli Was Born In Delhi And Playes Cricket For India")

if st.button("Analyze Text"):
    if text_input.strip():
        doc = nlp(text_input)
        
        # 1. Visualization (User Friendly)
        st.subheader("Visual Analysis")
        ent_html = displacy.render(doc, style="ent")
        st.write(ent_html, unsafe_allow_html=True)
        
        # 2. Data Table
        st.subheader("Entity Details")
        entities = [[ent.text, ent.label_, spacy.explain(ent.label_)] for ent in doc.ents]
        
        if entities:
            st.table({"Entity": [e[0] for e in entities], 
                      "Label": [e[1] for e in entities], 
                      "Description": [e[2] for e in entities]})
        else:
            st.info("No entities found.")
    else:
        st.warning("Please enter some text.")
