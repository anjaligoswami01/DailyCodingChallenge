from preprocessing import preprocess_text

def preprocess_pipeline(data):
    processed_data = []

    for i, text in enumerate(data):
        processed = preprocess_text(text)
        processed_data.append(processed)

        print(f"\n--- News {i+1} ---")
        print("Original:", text)
        print("Processed:", processed)

    return processed_data