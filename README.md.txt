📰 Fake News Detection using Machine Learning

This project detects whether a news article is *real* or *fake* using traditional machine learning algorithms and NLP techniques.

Features
- Data preprocessing: cleaning, tokenization, stopword removal
- Feature extraction using TF-IDF vectorization
- Classification using algorithms such as:
  - Logistic Regression
  - Naive Bayes
  - Random Forest
  - Passive Aggressive Classifier
- Achieved up to 96% accuracy

Dataset
- Source: [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Contains labeled news articles (real and fake)

Installation
1. Clone this repository:
  
   git clone https://github.com/afrin2315/fake-news-detection.git

2. Install dependencies:

pip install -r requirements.txt



Usage

Run the main script:

python fake_news_detection.py
You can modify the code or add scripts for training and evaluation.

Results

Logistic Regression with TF-IDF features gave the best accuracy (~96%)
Visualization of confusion matrix and classification reports included


Future Work

Deploy as a web app using Streamlit or Flask
Add user input interface to predict news real/fake on the fly
