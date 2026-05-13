# 🔹 1. Import Libraries

import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer


# 🔹 2. Download NLTK Data

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


# 🔹 3. Load Dataset

df = pd.read_csv("ta1.csv")

print("First 5 Rows:")
print(df.head())


# 🔹 4. Extract Text Column

text = df['text'][0]

print("\nOriginal Text:")
print(text)


# 🔹 5. Tokenization

tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)


# 🔹 6. Stopwords Removal

stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in tokens
    if word.lower() not in stop_words
]

print("\nAfter Stopwords Removal:")
print(filtered_words)


# 🔹 7. POS Tagging

pos_tags = pos_tag(filtered_words)

print("\nPOS Tags:")
print(pos_tags)


# 🔹 8. Stemming

stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in filtered_words
]

print("\nStemmed Words:")
print(stemmed_words)


# 🔹 9. Lemmatization

lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("\nLemmatized Words:")
print(lemmatized_words)


# 🔹 10. TF-IDF

documents = df['text'].astype(str)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
