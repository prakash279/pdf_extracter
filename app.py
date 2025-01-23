import streamlit as st
import pdfplumber
import pandas as pd
import spacy
import os
import json

nlp = spacy.load("trained_ner_model")

def custom_function(text):
    doc = nlp(text)

    # Extract entities
    extracted_data = {}
    for ent in doc.ents:
        extracted_data[ent.label_] = ent.text
        
    return extracted_data

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

DATA_FILE = "data.json"

# Initialize or load data from the JSON file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Load existing data from JSON file
with open(DATA_FILE, "r") as f:
    stored_data = json.load(f)

# Streamlit app layout
st.title("PDF Data Extractor and Viewer")

uploaded_files = st.file_uploader(
    "Upload PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Extract text using the extraction function
        text = extract_text_from_pdf(uploaded_file)
        
        # Process text with custom function to get structured data
        result = custom_function(text)
        
        # Append result to the stored data
        stored_data.append(result)
        
        # Save updated data to the JSON file
        with open(DATA_FILE, "w") as f:
            json.dump(stored_data, f)
    
    st.success("Data has been processed and saved!")

# Load and display data from the JSON file
if stored_data:
    st.write("Stored Data:")
    df = pd.DataFrame(stored_data)
    st.dataframe(df)
else:
    st.write("No data available yet.")
