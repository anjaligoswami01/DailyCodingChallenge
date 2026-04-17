import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def tokenize(text):
    return text.split()


def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]


def stem_tokens(tokens):
    return [stemmer.stem(word) for word in tokens]


def preprocess_pipeline(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)
    return " ".join(tokens)