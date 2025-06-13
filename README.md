📰 Fake News Detection using Machine Learning & NLP
An end-to-end Fake News Detection system leveraging Natural Language Processing (NLP) and Machine Learning to classify news articles as real or fake with high accuracy. This project includes data preprocessing, model training, and a user-friendly Streamlit web app for real-time news validation.

📌 Project Highlights
✅ Cleaned and preprocessed real-world datasets (True.csv, Fake.csv)

✅ Applied NLP techniques: tokenization, stopwords removal, and vectorization

✅ Trained a PassiveAggressiveClassifier achieving 99% accuracy

✅ Developed an interactive Streamlit app for live news prediction

✅ Saved and deployed the trained model using joblib

🗂 Project Structure
graphql
Copy
Edit
fake-news-detection/
├── apps/               # Streamlit application code
│   └── app.py
├── models/             # Saved machine learning model
│   └── fake_news_model.pkl
├── notebooks/          # Jupyter notebooks for exploration and training
│   └── training.ipynb
├── Fake.csv            # Fake news dataset
├── True.csv            # Real news dataset
└── README.md           # Project overview and instructions
🚀 How to Run
bash
Copy
Edit
# Clone the repo
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run apps/app.py
👩‍💻 Author
Afrin Kousar — AIML Student, 3rd Year
🔗 LinkedIn
✉ afrinkousar98@gmail.com
