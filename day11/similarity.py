# Import required libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
doc1 = "Data engineering is the foundation of modern analytics."
doc2 = "Data engineering plays a key role in building analytics systems."

# Step 1: Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

# Step 2: Compute cosine similarity
similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

# Output result
print("Cosine Similarity Score:", similarity_score[0][0])