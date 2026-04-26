import numpy as np

def normalize_embeddings(embeddings):
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    return embeddings / norms

def cosine_similarity_matrix(embeddings):
    normalized = normalize_embeddings(embeddings)
    return np.dot(normalized, normalized.T)

def mean_embedding(embeddings):
    return np.mean(embeddings, axis=0)

def scale_embeddings(embeddings, factor=2):
    return embeddings * factor