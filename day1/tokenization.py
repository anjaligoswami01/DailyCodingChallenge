##TASK 1

text = "Python is easy and Python is powerful"

# Step 1: Tokenization
def tokenize(text):
    text = text.lower()
    return text.split()

# Step 2: Stopword removal
stopwords = ["is", "and", "the", "in"]

def remove_stopwords(words):
    result = []
    for word in words:
        if word not in stopwords:
            result.append(word)
    return result

# Step 3: Word frequency
def word_count(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# Run all steps
tokens = tokenize(text)
filtered = remove_stopwords(tokens)
frequency = word_count(filtered)

print("Tokens:", tokens)
print("Filtered Words:", filtered)
print("Word Frequency:", frequency)