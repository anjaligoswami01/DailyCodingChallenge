import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Sample paragraph
text = """Natural Language Processing is amazing. 
It helps computers understand human language. 
Let's learn tokenization using NLTK!"""

# Sentence Tokenization
sentences = sent_tokenize(text)

print("Sentence Tokenization:")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. {sentence}")

print("\n----------------------\n")

# Word Tokenization
print("Word Tokenization:")
for sentence in sentences:
    words = word_tokenize(sentence)
    print(words)