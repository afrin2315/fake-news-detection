📰 Fake News Detection using Machine Learning & NLP

This project is an end-to-end Fake News Detection system built using **Natural Language Processing (NLP)** and **Machine Learning**. It allows users to enter a news article and predicts whether it's *Fake* or *Real*.

🔍 Features

- Cleaned & Preprocessed real-world datasets (True.csv, Fake.csv)
- NLP techniques: Tokenization, Stopwords Removal, TF-IDF Vectorization
- Model: XGBoost Classifier
- Web App: Built using Flask
- Deployment Ready (Render-compatible)

🛠️ Tech Stack

- Python
- Flask
- NLTK
- Scikit-learn
- XGBoost
- HTML/CSS (Jinja2 templates)

🚀 How to Run Locally

1. Clone this repo:
   
   git clone https://github.com/afrin2315/fake-news-detection.git
   cd fake-news-detection

2. Install requirements:

pip install -r requirements.txt

3. Run the app:

python app.py

4. Open in browser:

http://127.0.0.1:5000


📦 Files
app.py: Flask backend

tfidf_vectorizer.pkl: Pre-trained TF-IDF vectorizer

xgb_model.json: Trained XGBoost model

templates/index.html: Frontend page

🧠 Prediction Logic
Preprocess text input (lowercase, remove punctuations, stopwords)
Vectorize using saved TF-IDF model
Predict with the loaded XGBoost classifier

👩‍💻 Author

- **Afrin Kousar**
- 📧 Email: afrinkousar98@gmail.com
- 🔗 LinkedIn: [afrin-kousar](https://www.linkedin.com/in/afrin-kousar)
- 🐙 GitHub: [afrin2315](https://github.com/afrin2315)


