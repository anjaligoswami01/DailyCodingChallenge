import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Wow!!! I bought this product for Rs.999 🤩 and it's AMAZING!!! 100% recommended... but delivery took 3 days 😕"

# Step 1: Lowercase
text = text.lower()

# Step 2: Remove numbers
text = re.sub(r'\d+', '', text)

# Step 3: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 4: Tokenize
words = word_tokenize(text)

# Step 5: Remove stopwords
stop_words = set(stopwords.words('english'))
clean_words = [word for word in words if word not in stop_words]

# Output
print("Cleaned Words:\n", clean_words)