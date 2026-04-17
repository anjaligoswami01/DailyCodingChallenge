from preprocess import preprocess_text
from bow import create_bow
from tfidf import compute_tf, compute_idf, compute_tfidf

def main():

    data = [
        "Natural language processing is fun and exciting.",
        "Machine learning makes NLP powerful.",
        "Text data needs preprocessing before feature extraction."
    ]

    processed_docs = []

    print("\n--- Preprocessing ---")
    for line in data:
        tokens = preprocess_text(line)
        processed_docs.append(tokens)
        print(tokens)

    print("\n--- Bag of Words ---")
    for doc in processed_docs:
        bow = create_bow(doc)
        print(bow)

    print("\n--- TF-IDF ---")
    idf = compute_idf(processed_docs)

    for doc in processed_docs:
        tf = compute_tf(doc)
        tfidf = compute_tfidf(tf, idf)
        print(tfidf)


if __name__ == "__main__":
    main()