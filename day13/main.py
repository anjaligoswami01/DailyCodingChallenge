from preprocess import preprocess_pipeline
from vectorizer import TextVectorizer
from utils import print_processed_data, print_features


def main():
    messages = [
        "Congratulations! You won a FREE lottery. Call now!",
        "Hey, are we still meeting today?",
        "Win cash prizes now!!! Limited offer!!!",
        "Let's complete the project report."
    ]

    # Step 1: Preprocess
    processed = [preprocess_pipeline(msg) for msg in messages]

    # Step 2: Vectorize
    vectorizer = TextVectorizer()
    features = vectorizer.fit_transform(processed)

    # Step 3: Output
    print_processed_data(processed)
    print_features(features)


if __name__ == "__main__":
    main()