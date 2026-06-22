# ============================================================
# AI-POWERED PARAPHRASING TOOL
# Uses:
#   - T5 Transformer (Paraphrasing)
#   - TextBlob (Grammar Correction)
#   - BLEU Score
#   - ROUGE Score
#   - Semantic Similarity
# ============================================================

# ------------------------------------------------------------
# STEP 1: INSTALL REQUIRED LIBRARIES
# ------------------------------------------------------------

# Run these commands once in terminal or Colab:

# pip install transformers sentencepiece torch
# pip install textblob nltk rouge-score sentence-transformers

# ------------------------------------------------------------
# STEP 2: IMPORT LIBRARIES
# ------------------------------------------------------------

import nltk
from textblob import TextBlob
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer, util

# Download NLTK data
nltk.download('punkt')

# ------------------------------------------------------------
# STEP 3: LOAD T5 MODEL
# ------------------------------------------------------------

print("Loading T5 model...")

model_name = "ramsrigouthamg/t5_paraphraser"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model Loaded Successfully!\n")

# ------------------------------------------------------------
# STEP 4: PARAPHRASING FUNCTION
# ------------------------------------------------------------

def paraphrase_text(text):

    prompt = "paraphrase: " + text + " </s>"

    encoding = tokenizer.encode_plus(
        prompt,
        max_length=256,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )

    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]

    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1
    )

    paraphrased = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    )

    return paraphrased

# ------------------------------------------------------------
# STEP 5: GRAMMAR CORRECTION
# ------------------------------------------------------------

def grammar_correction(text):
    corrected = str(TextBlob(text).correct())
    return corrected

# ------------------------------------------------------------
# STEP 6: BLEU SCORE
# ------------------------------------------------------------

def calculate_bleu(reference, candidate):

    reference_tokens = [reference.split()]
    candidate_tokens = candidate.split()

    score = sentence_bleu(
        reference_tokens,
        candidate_tokens
    )

    return round(score, 4)

# ------------------------------------------------------------
# STEP 7: ROUGE SCORE
# ------------------------------------------------------------

def calculate_rouge(reference, candidate):

    scorer = rouge_scorer.RougeScorer(
        ['rouge1', 'rouge2', 'rougeL'],
        use_stemmer=True
    )

    scores = scorer.score(reference, candidate)

    return {
        "ROUGE-1": round(scores['rouge1'].fmeasure, 4),
        "ROUGE-2": round(scores['rouge2'].fmeasure, 4),
        "ROUGE-L": round(scores['rougeL'].fmeasure, 4)
    }

# ------------------------------------------------------------
# STEP 8: SEMANTIC SIMILARITY
# ------------------------------------------------------------

semantic_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def semantic_similarity(text1, text2):

    embeddings = semantic_model.encode(
        [text1, text2],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1]
    )

    return round(float(similarity), 4)

# ------------------------------------------------------------
# STEP 9: MAIN PROGRAM
# ------------------------------------------------------------

def main():

    print("=" * 60)
    print("AI-POWERED PARAPHRASING TOOL")
    print("=" * 60)

    input_text = input("\nEnter text to paraphrase:\n\n")

    print("\nGenerating paraphrase...\n")

    paraphrased_text = paraphrase_text(input_text)

    corrected_text = grammar_correction(
        paraphrased_text
    )

    bleu_score = calculate_bleu(
        input_text,
        corrected_text
    )

    rouge_scores = calculate_rouge(
        input_text,
        corrected_text
    )

    similarity_score = semantic_similarity(
        input_text,
        corrected_text
    )

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    print("\nOriginal Text:")
    print(input_text)

    print("\nParaphrased Text:")
    print(corrected_text)

    print("\nEvaluation Metrics")
    print("-" * 40)

    print(f"BLEU Score: {bleu_score}")

    print(f"ROUGE-1: {rouge_scores['ROUGE-1']}")
    print(f"ROUGE-2: {rouge_scores['ROUGE-2']}")
    print(f"ROUGE-L: {rouge_scores['ROUGE-L']}")

    print(f"Semantic Similarity: {similarity_score}")

    print("\nProcess Completed Successfully!")

# ------------------------------------------------------------
# RUN PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
    