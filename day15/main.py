from embeddings import get_sample_embeddings
from operations import (
    normalize_embeddings,
    cosine_similarity_matrix,
    mean_embedding,
    scale_embeddings
)
from utils import print_section

def main():
    embeddings = get_sample_embeddings()

    normalized = normalize_embeddings(embeddings)
    similarity = cosine_similarity_matrix(embeddings)
    mean_vec = mean_embedding(embeddings)
    scaled = scale_embeddings(embeddings)

    print_section("Original Embeddings", embeddings)
    print_section("Normalized Embeddings", normalized)
    print_section("Cosine Similarity Matrix", similarity)
    print_section("Mean Embedding", mean_vec)
    print_section("Scaled Embeddings", scaled)

if __name__ == "__main__":
    main()