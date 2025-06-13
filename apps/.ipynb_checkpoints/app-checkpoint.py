import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("../models/fake_news_model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

# App UI
st.title("📰 Fake News Detector")
st.write("Enter a news article below and I'll predict whether it's *Real* or *Fake*.")

# Text input
user_input = st.text_area("Paste the news content here:", height=250)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some news content.")
    else:
        # Transform and predict
        vector_input = vectorizer.transform([user_input])
        prediction = model.predict(vector_input)[0]
        
        # Output result
        if prediction == 1:
            st.success("✅ It's Real News!")
        else:
            st.error("🚨 It's Fake News!")