import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Download required data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    sentences = sent_tokenize(text)

    processed_sentences = []

    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word for word in words if word not in string.punctuation]
        words = [word for word in words if word not in stop_words]
        words = [lemmatizer.lemmatize(word) for word in words]

        processed_sentences.append(words)

    return processed_sentences