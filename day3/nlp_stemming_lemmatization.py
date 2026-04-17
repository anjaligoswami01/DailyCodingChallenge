# 1. Imports
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# 2. Downloads (only first time)
nltk.download('punkt')
nltk.download('wordnet')

# 3. Sample Dataset
reviews = [
    "The product quality is amazing and working perfectly",
    "I was disappointed with the packaging and delivery",
    "Excellent performance and very durable product"
]

# 4. Initialize tools
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# 5. Function
def process_text(text):
    words = word_tokenize(text.lower())
    stemmed = [stemmer.stem(word) for word in words]
    lemmatized = [lemmatizer.lemmatize(word) for word in words]
    return stemmed, lemmatized

# 6. Run
for review in reviews:
    stemmed, lemmatized = process_text(review)
    print("\nReview:", review)
    print("Stemmed:", stemmed)
    print("Lemmatized:", lemmatized)