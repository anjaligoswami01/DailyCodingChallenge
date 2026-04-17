import math
from collections import Counter

def compute_tf(tokens):
    tf_dict = {}
    total_words = len(tokens)
    word_count = Counter(tokens)

    for word, count in word_count.items():
        tf_dict[word] = count / total_words

    return tf_dict


def compute_idf(docs):
    N = len(docs)
    idf_dict = {}

    all_words = set([word for doc in docs for word in doc])

    for word in all_words:
        containing_docs = sum(1 for doc in docs if word in doc)
        idf_dict[word] = math.log(N / (1 + containing_docs))

    return idf_dict


def compute_tfidf(tf, idf):
    return {word: tf[word] * idf.get(word, 0) for word in tf}