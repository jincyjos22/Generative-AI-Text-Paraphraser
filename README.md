# 🚀 Generative AI Text Paraphraser

### Transformer-based NLP system for paraphrasing, grammar correction, and semantic evaluation

A transformer-based NLP tool that rewrites text while preserving meaning, improving clarity, and ensuring originality — built with Hugging Face Transformers, LanguageTool, and Sentence-Transformers.

**Author:** Muhsina Safeeth

---

## 📌 Overview

This project is a Generative AI module assignment that implements an end-to-end paraphrasing pipeline. It uses the **T5-small** transformer model to generate paraphrases, applies automated grammar and fluency correction, and evaluates output quality using BLEU, ROUGE-L, and semantic similarity metrics.

---

## ✨ Features

- 🔄 Transformer-based paraphrasing using T5-small
- ✅ Grammar & spelling correction via LanguageTool
- 📊 Evaluation using BLEU, ROUGE-L, and semantic similarity
- ⚡ Lightweight and CPU-friendly (no GPU required)
- 📓 Clean and well-structured notebook implementation

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Model | T5-small (Hugging Face Transformers) |
| Grammar Check | LanguageTool |
| Semantic Evaluation | Sentence-Transformers |
| Metrics | BLEU, ROUGE-L, Semantic Similarity |

---

## 🏗 Architecture

User Input  
⬇  
Text Preprocessing  
⬇  
T5-small Transformer Model  
⬇  
Grammar Correction (LanguageTool)  
⬇  
Evaluation Metrics (BLEU | ROUGE-L | Semantic Similarity)  
⬇  
Final Output  

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install transformers sentencepiece torch
pip install textblob nltk rouge-score sentence-transformers language-tool-python
```

### 2. Run the project
```bash
python main.py
```

OR

```bash
jupyter notebook
```

---

## 📊 Evaluation Metrics

| Metric | Purpose |
|---|---|
| BLEU | Word overlap similarity |
| ROUGE-L | Sequence overlap |
| Semantic Similarity | Meaning preservation |

> Semantic similarity is the most important metric as paraphrasing focuses on preserving meaning.

---

## 🧪 Example

**Input:**
Artificial intelligence is transforming many industries by automating tasks, improving decision-making, and enabling new products and services.

**Output:**
AI is reshaping industries by automating work, improving decisions, and enabling new services.

---

## 📈 Project Outcomes

- Meaning-preserving paraphrasing
- Grammar correction automation
- Semantic evaluation pipeline
- Transformer-based NLP workflow
- Ready for deployment improvements

---

## 🛣 Roadmap

- Multiple paraphrase generation
- Fine-tuning on custom datasets
- Plagiarism detection module
- Web API / Streamlit deployment
- Multilingual support

---

## 📚 References

1. T5: Exploring Transfer Learning (Raffel et al.)
2. Hugging Face Transformers
3. LanguageTool
4. Sentence-Transformers
5. BLEU Score (Papineni et al.)
6. ROUGE Metric (Lin)

---

## 📄 License

This project is licensed under the MIT License.
