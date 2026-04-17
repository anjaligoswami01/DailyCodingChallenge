# 🚀 NLP Pipeline 

## 📌 Overview

This project demonstrates how to build a **reusable NLP (Natural Language Processing) pipeline** using a single Python file. It processes raw text data and converts it into structured numerical features that can be used in machine learning models.

---

## ⚙️ Features

* ✅ Text Cleaning (lowercasing, punctuation removal)
* ✅ Tokenization
* ✅ Stopword Removal
* ✅ Feature Extraction using Bag of Words (CountVectorizer)
* ✅ Fully reusable pipeline function

---

## 🧠 How It Works

The pipeline follows these steps:

```
Raw Text → Cleaning → Tokenization → Stopword Removal → Feature Extraction
```

---

## 📁 Project Structure

```
nlp-pipeline/
│
├── nlp_pipeline.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/anjaligoswami01/nlp-pipeline.git
cd nlp-pipeline
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script:

```bash
python nlp_pipeline.py
```

---

## 📊 Example Output

```
Processed Text:
- love learning nlp
- nlp interesting powerful
- ai nlp transforming world

Feature Names:
['ai' 'interesting' 'learning' 'love' 'nlp' 'powerful' 'transforming' 'world']

Feature Matrix:
[[0 0 1 1 1 0 0 0]
 [0 1 0 0 1 1 0 0]
 [1 0 0 0 1 0 1 1]]
```

---

## 💡 Key Learnings

* Built a modular NLP pipeline inside a single Python file
* Understood core text preprocessing techniques
* Learned how text is converted into numerical features
* Improved code reusability and workflow design

---

## 🚀 Future Improvements

* 🔹 Add Lemmatization (NLTK / SpaCy)
* 🔹 Use TF-IDF Vectorizer
* 🔹 Accept user input dynamically
* 🔹 Convert into REST API using Flask or FastAPI
* 🔹 Apply on real-world datasets

---

## 🧑‍💻 Author

ANJALI GOSWAMI

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
