# 📌 AI-Powered Paraphrasing Tool

## 🚀 Overview

This project is an AI-based Natural Language Processing (NLP) system that performs intelligent text paraphrasing using Transformer models. It also includes grammar correction and automatic evaluation of output quality using NLP metrics.

It is designed as a complete NLP mini-project combining:

- Deep Learning (Transformers)
- NLP preprocessing
- Text evaluation metrics
- Grammar correction system

## ✨ Key Features

### 🧠 1. AI Paraphrasing
- Uses T5 Transformer model
- Generates multiple paraphrased versions of input text
- Maintains original meaning while changing structure

### ✍️ 2. Grammar Correction
- Uses LanguageTool
- Detects grammatical errors
- Provides corrected output text

### 📊 3. Evaluation System
Automatically evaluates paraphrases using:

- BLEU Score → Word overlap accuracy  
- ROUGE-L Score → Sequence similarity  
- Semantic Similarity → Meaning preservation (Sentence Transformers)

## ⚙️ Technologies Used

- Python 🐍  
- Hugging Face Transformers 🤗  
- T5 Model (`ramsrigouthamg/t5_paraphraser`)  
- Sentence Transformers  
- NLTK  
- ROUGE Score  
- LanguageTool  
- TextBlob (optional)

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/paraphrasing-tool.git
cd paraphrasing-tool
