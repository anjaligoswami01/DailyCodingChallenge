# Step 1: Import library
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Step 2: Download tokenizer (only first time)
nltk.download('punkt')

# Step 3: Sample paragraph
text = """Natural Language Processing is amazing.
It helps computers understand human language.
Let's learn tokenization using NLTK!"""

# Step 4: Sentence Tokenization
sentences = sent_tokenize(text)

print("Sentence Tokenization:\n")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. {sentence}")

# Step 5: Word Tokenization
print("\nWord Tokenization:\n")

for sentence in sentences:
    words = word_tokenize(sentence)
    print(words)