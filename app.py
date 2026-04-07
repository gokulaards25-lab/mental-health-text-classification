import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = pickle.load(open("svm_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Preprocessing
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# UI
st.title("🧠 Mental Health Text Classifier")

user_input = st.text_area("Enter your text:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        clean_text = preprocess(user_input)
        vector = vectorizer.transform([clean_text])
        prediction = model.predict(vector)

        st.success(f"Prediction: {prediction[0]}")
