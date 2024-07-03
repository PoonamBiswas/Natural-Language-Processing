import streamlit as st
import spacy

# Load the trained NER model
nlp = spacy.load("/Users/poonam/Desktop/MRU/NLP_deployment/stop_ner31")

# Define a function to test the NER model on a new sentence
def test_ner(sentence):
    doc = nlp(sentence)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Set the title of the Streamlit app
st.title("Stop Name Recognition")

# Create a text input field for the user to enter a sentence
sentence_input = st.text_input("Enter a sentence:")

# If the user has entered a sentence, run the NER model and display the results
if sentence_input:
    entities = test_ner(sentence_input)
    if entities:
        for entity in entities:
            st.write(f"- Entity: {entity[0]}, Label: {entity[1]}")
    else:
        st.write("No entities found.")
