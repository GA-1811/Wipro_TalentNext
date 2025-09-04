#Perform Text Preprocessing on SMSSpamCollection Dataset.

import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

nltk.download('stopwords')

df = pd.read_csv('SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)

    tokens = text.split()

    processed = []
    for word in tokens:
        if word not in stop_words:
            stemmed = stemmer.stem(word)
            processed.append(stemmed)

    return ' '.join(processed)

df['processed_message'] = df['message'].apply(preprocess_text)

print(df[['label', 'processed_message']].head())
