🤖 AI-Powered Paraphrasing Tool










📌 Overview

This project is an AI-powered paraphrasing tool built using state-of-the-art Transformer models (T5) from Hugging Face.

It takes an input text and generates a meaning-preserving, fluent, and improved paraphrased version using deep learning.

Additionally, it evaluates output quality using NLP metrics such as BLEU, ROUGE, and Semantic Similarity.

🚀 Features
✍️ AI-based text paraphrasing using T5 Transformer
🧠 Preserves original meaning while improving clarity
📊 Automatic evaluation using:
BLEU Score
ROUGE-L Score
Semantic Similarity (Sentence-BERT)
🔍 Grammar correction using TextBlob
💻 Fully console-based (no GUI required)
⚡ Lightweight and easy to run
🧠 Technologies Used
Python 🐍
Hugging Face Transformers 🤗
PyTorch 🔥
NLTK 📚
TextBlob ✏️
SentenceTransformers 🧬
🏗️ Project Architecture
Input Text
   ↓
T5 Transformer Model (Paraphrasing)
   ↓
Generated Paraphrase
   ↓
Grammar Correction (TextBlob)
   ↓
Evaluation Module
   ├── BLEU Score
   ├── ROUGE Score
   └── Semantic Similarity
   ↓
Final Output
📦 Installation

Clone the repository:

git clone https://github.com/your-username/paraphrasing-tool.git
cd paraphrasing-tool

Install dependencies:

pip install transformers sentencepiece torch
pip install textblob nltk rouge-score sentence-transformers

Download NLTK data:

import nltk
nltk.download('punkt')
▶️ How to Run

Run the Python script:

python paraphrasing_tool.py

Or run in Jupyter Notebook:

AI_Paraphrasing_Tool.ipynb
🧪 Sample Output
Input:
Machine learning enables computers to learn from data and make predictions.
Output:
Machine learning allows computers to learn from data and make predictions.
📊 Evaluation Metrics
Metric	Description
BLEU	Measures word overlap with reference
ROUGE-L	Measures longest common subsequence
Semantic Similarity	Measures meaning similarity using embeddings
📉 Limitations
Grammar correction is basic (TextBlob-based)
No model fine-tuning (uses pre-trained T5)
BLEU is not ideal for paraphrasing evaluation
Performance depends on input sentence complexity
🔮 Future Improvements
Fine-tuning T5 on paraphrase datasets
Replace TextBlob with LanguageTool
Add web interface using Streamlit
Support multiple paraphrasing styles (formal, casual, simple)
Add API deployment using FastAPI
👨‍💻 Author

Jincy Jos

📜 License

This project is licensed under the MIT License.

⭐ If you like this project

Give it a ⭐ on GitHub and improve it further!
