# Import libraries
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Download stopwords (run once)
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Step 1: Text Cleaning Function
def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text

# Step 2: Tokenization + Stopword Removal
def tokenize_text(text):
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Step 3: NLP Pipeline Function (Reusable)
def nlp_pipeline(text_list):
    processed_texts = []

    for text in text_list:
        cleaned = clean_text(text)
        tokens = tokenize_text(cleaned)
        processed_texts.append(" ".join(tokens))

    # Step 4: Feature Extraction (Bag of Words)
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(processed_texts)

    return {
        "processed_text": processed_texts,
        "feature_names": vectorizer.get_feature_names_out(),
        "feature_matrix": features.toarray()
    }

# Example Usage
texts = [
    "I love learning NLP!",
    "NLP is very interesting and powerful."
]

result = nlp_pipeline(texts)

print("Processed Text:", result["processed_text"])
print("Feature Names:", result["feature_names"])
print("Feature Matrix:\n", result["feature_matrix"])