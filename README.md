# 🚀 AI-Powered Paraphrasing Tool

### Transformer-Based NLP System for Text Paraphrasing, Grammar Correction, and Evaluation

---

## 📌 Overview

The AI-Powered Paraphrasing Tool is a Python-based Natural Language Processing (NLP) application that rewrites text while preserving its original meaning. The tool leverages a Transformer-based T5 model to generate paraphrased content and uses grammar correction techniques to improve fluency and readability.

Additionally, the system evaluates the generated output using standard NLP metrics such as BLEU, ROUGE, and Semantic Similarity.

This project demonstrates the practical application of Generative AI and Transformer models for text generation tasks.

---

## ✨ Features

* 🔁 Text paraphrasing using the T5 Transformer model
* ✍️ Grammar correction using TextBlob
* 📊 BLEU score evaluation
* 📈 ROUGE score evaluation
* 🧠 Semantic similarity measurement using Sentence Transformers
* 💻 Console-based input and output
* ⚡ Fast and lightweight implementation in Python

---

## 🛠️ Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* TextBlob
* NLTK
* ROUGE Score
* Sentence Transformers

---

## 📂 Project Structure

```text
AI-Powered-Paraphrasing-Tool
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📦 Installation

Install the required libraries:

```bash
pip install transformers sentencepiece torch
pip install textblob nltk rouge-score sentence-transformers
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Execute the following command:

```bash
python main.py
```

The application will prompt:

```text
Enter text to paraphrase:
```

Enter any sentence or paragraph and press Enter.

---

## 🔍 Sample Input

```text
Artificial Intelligence is transforming the way people work and communicate.
```

## 🔍 Sample Output

```text
Original Text:
Artificial Intelligence is transforming the way people work and communicate.

Paraphrased Text:
Artificial intelligence is changing how individuals communicate and perform their work.

BLEU Score: 0.42
ROUGE-1: 0.70
ROUGE-2: 0.51
ROUGE-L: 0.68
Semantic Similarity: 0.93
```

---

## 📊 Evaluation Metrics

### BLEU Score

Measures the similarity between the original text and the paraphrased output based on word overlap.

### ROUGE Score

Evaluates the quality of generated text by comparing overlapping words and sequences.

### Semantic Similarity

Measures how closely the meaning of the paraphrased text matches the original text using sentence embeddings.

---

## 🔄 Workflow

1. User enters input text.
2. T5 Transformer generates a paraphrased version.
3. TextBlob performs grammar correction.
4. BLEU score is calculated.
5. ROUGE score is calculated.
6. Semantic similarity score is computed.
7. Results are displayed in the console.

---

## 🎯 Learning Outcomes

* Understanding Transformer-based text generation
* Applying Generative AI techniques
* Working with Hugging Face Transformer models
* Implementing text evaluation metrics
* Measuring semantic similarity using sentence embeddings

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Jincy Jos**

Generative AI Module End Assignment
