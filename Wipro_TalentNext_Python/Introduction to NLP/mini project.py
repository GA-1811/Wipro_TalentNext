#Create a model that will predict the rating based on the feedback of the customer. 
# Feature: Text 
# Label: Star


import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

nltk.download('stopwords')

df = pd.DataFrame({
    'feedback': [
        "Amazing product, loved it!",
        "Terrible experience, very disappointed.",
        "Okayish, could be better.",
        "Great value for money.",
        "Worst service ever."
    ],
    'star': [5, 1, 3, 4, 1]
})

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    tokens = text.split()
    filtered = []
    for word in tokens:
        if word not in stop_words:
            stemmed = stemmer.stem(word)
            filtered.append(stemmed)
    return ' '.join(filtered)

df['cleaned'] = df['feedback'].apply(preprocess)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned'])

y = df['star']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
