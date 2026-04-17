def print_processed_data(data):
    print("\n--- Processed Text ---")
    for i, text in enumerate(data, 1):
        print(f"{i}. {text}")


def print_features(features):
    print("\n--- Feature Matrix ---")
    print(features.toarray())