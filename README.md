# Generative-AI-Text-Paraphraser

## 📌 Overview

The AI-Powered Paraphrasing Tool is a Transformer-based NLP system that rewrites input text while preserving its meaning. It also performs grammar correction and evaluates output quality using standard NLP metrics.

Built using T5 Transformer models, this project demonstrates a complete NLP pipeline including generation, correction, and evaluation.

## ✨ Features

- 🔁 AI-based paraphrasing using T5 Transformer  
- ✍️ Grammar correction using TextBlob  
- 📊 Evaluation metrics:
  - BLEU Score  
  - ROUGE Score  
  - Semantic Similarity  
- 🧠 Sentence embedding comparison using SentenceTransformers  
- ⚡ Lightweight pipeline (no Java required)  
- 🧪 Supports multiple test cases  

## 🛠️ Tech Stack

- Python 3  
- Hugging Face Transformers  
- PyTorch  
- NLTK  
- TextBlob  
- ROUGE Score  
- Sentence-Transformers  

## 📂 Project Structure

AI-Paraphrasing-Tool/

├── paraphrasing_tool.py   # Main pipeline code  
├── requirements.txt       # Dependencies  
└── README.md              # Project documentation  

## ⚙️ Installation

1. Clone the repository  
```bash
git clone https://github.com/your-username/AI-Paraphrasing-Tool.git
cd AI-Paraphrasing-Tool
```

2. Install dependencies  
```bash
pip install transformers sentencepiece torch
pip install textblob nltk rouge-score sentence-transformers
```

3. Download NLTK data  
```python
import nltk
nltk.download('punkt')
```

## 🚀 How It Works

- Input text is passed into a T5 Transformer model  
- Model generates multiple paraphrased versions  
- Each output is:
  - Grammatically corrected (TextBlob)  
  - Evaluated using:
    - BLEU score  
    - ROUGE score  
    - Semantic similarity (Sentence-BERT)  
- Final results are displayed with metrics  

## ▶️ Usage

```python
from paraphrasing_tool import run_pipeline

text = "Machine learning enables computers to learn from data."
run_pipeline(text, n=2)
```

## 📊 Example Output

ORIGINAL TEXT:
Machine learning enables computers to learn from data...

PARAPHRASE:
Machine learning allows systems to learn from data...

METRICS:
BLEU  : 0.42  
ROUGE : 0.78  
SIM   : 0.91  

## 🧠 Model Used

- T5 Paraphraser: ramsrigouthamg/t5_paraphraser  
- Sentence Embedding Model: all-MiniLM-L6-v2  

## 📈 Future Improvements

- 🌐 Web UI using Streamlit or Flask  
- 🔥 Better grammar correction using LanguageTool API  
- 📊 Advanced evaluation dashboard  
- 💾 Save paraphrased outputs as dataset  
- ⚡ Faster inference optimization  

## 👨‍💻 Author

Jincy Jos  

## 📜 License

This project is licensed under the MIT License.
