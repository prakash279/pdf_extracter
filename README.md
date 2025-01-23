# PDF Data Extractor and Viewer

This repository contains a Streamlit application that extracts text from uploaded PDF files and uses a custom NER (Named Entity Recognition) model to identify entities in the text. The extracted data is stored in a JSON file and displayed in a tabular format within the app.

---

## Features
- Upload multiple PDF files for text extraction.
- Extract entities using a custom NER model built with spaCy.
- Save extracted data persistently in a `data.json` file.
- Display stored data in a table within the Streamlit app.

---

## Requirements

### Python Libraries
Make sure you have the following libraries installed:

- `streamlit`
- `pdfplumber`
- `pandas`
- `spacy`

You can install these dependencies using the following command:
```bash
pip install streamlit pdfplumber pandas spacy
```

### Trained NER Model
- The application requires a spaCy NER model (`trained_ner_model`) to extract entities from text.
- Ensure that the model is available and loaded correctly in the code.

If you need to train a custom NER model, follow the official spaCy documentation: [Training spaCy Models](https://spacy.io/usage/training)

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/prakash279/pdf_extracter.git
cd odf_extracter
```

### 2. Add Your Trained NER Model
- Place your custom spaCy model directory in the project folder.
- Update the `nlp = spacy.load("trained_ner_model")` line in the code to point to your model's location if necessary.

### 3. Run the Application
Run the Streamlit app using the following command:
```bash
streamlit run app.py
```

### 4. Upload PDF Files
- Use the app interface to upload one or more PDF files.
- The extracted data will be processed and saved in the `data.json` file.

### 5. View Results
- The stored data is displayed in a table format within the app.
- The JSON file (`data.json`) maintains a persistent log of extracted data.

---

## File Structure

```
project-folder/
|-- app.py             # Main Streamlit application file
|-- data.json          # JSON file to store extracted data
|-- trained_ner_model/ # Directory containing your trained spaCy NER model
```

---

## Example Output

### Extracted Data
The `custom_function` processes the text and identifies entities, returning results in a dictionary format. Example output:

```json
[
    {
        "NAME": "Sarah Johnson",
        "PHONE": "+1 (415) 678-9923",
        "ADDRESS": "789 Mission St, San Francisco, CA",
        "ROLE": "Data Scientist"
    }
]
```


---

## Contact
If you have any questions or feedback, please contact me at [choudhary.prakash27903@example.com].

