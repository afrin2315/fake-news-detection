from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
import string
import pickle
import xgboost as xgb

app = Flask(__name__)

# Ensure nltk stopwords are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load vectorizer
try:
    with open(r'C:\Users\Fathma\OneDrive\Desktop\Fake-News_Detection\tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    print("Vectorizer file not found.")
    vectorizer = None

# Load XGBoost model
try:
    xgb_model = xgb.XGBClassifier()
    xgb_model.load_model(r'C:\Users\Fathma\OneDrive\Desktop\Fake-News_Detection\xgb_model.json')
except Exception as e:
    print("Error loading XGBoost model:", e)
    xgb_model = None

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Simple split instead of nltk.word_tokenize to avoid punkt error
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    news = None
    if request.method == 'POST':
        news = request.form.get('news')
        if not news:
            prediction = "Please enter some news text."
        elif not vectorizer or not xgb_model:
            prediction = "Model or vectorizer not loaded properly."
        else:
            processed_text = preprocess_text(news)
            vectorized_text = vectorizer.transform([processed_text])
            pred = xgb_model.predict(vectorized_text)[0]
            prediction = "Fake News" if pred == 1 else "Real News"
    return render_template('index.html', prediction=prediction, news=news)

if __name__ == '__main__':
    app.run(debug=True)
