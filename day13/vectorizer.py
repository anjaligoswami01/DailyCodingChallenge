from sklearn.feature_extraction.text import TfidfVectorizer


class TextVectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, corpus):
        return self.vectorizer.fit_transform(corpus)

    def transform(self, corpus):
        return self.vectorizer.transform(corpus)