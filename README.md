📰 Fake News Detection using Machine Learning & NLP

This project is an end-to-end Fake News Detection web app built using Natural Language Processing (NLP) and XGBoost classifier. It helps identify whether a given news headline/article is *Real* or *Fake* using advanced text vectorization and ML prediction.

🚀 Features
- Cleaned and preprocessed real-world dataset (True.csv & Fake.csv)
- TF-IDF vectorizer for feature extraction
- XGBoost model for accurate classification
- Flask-based web interface
- Deployed version using Render



🧠 How It Works
1. User enters news text in the input box.
2. The input is preprocessed (tokenized, lowercased, stopwords removed).
3. TF-IDF vectorizer converts text to numerical features.
4. XGBoost model predicts: `Fake News` or `Real News`.

⚙️ Tech Stack
- Python
- Flask
- XGBoost
- NLTK
- Scikit-learn
- HTML/CSS

🔗 Try the App
👉 [Live Demo (Render)](https://fake-news-afrin.onrender.com) <!-- Put your real link here -->

📦 Setup Locally

git clone https://github.com/afrin2315/fake-news-detection
cd fake-news-detection
pip install -r requirements.txt
python app.py

👤 Developed By
Afrin Kousar
📧 afrinkousar98@gmail.com
🔗 LinkedIn
