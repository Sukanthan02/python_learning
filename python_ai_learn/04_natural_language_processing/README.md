# Module 4: Natural Language Processing 📝

Natural Language Processing (NLP) is the branch of AI that allows computers to read, analyze, interpret, and generate human languages. This module demonstrates the transition from traditional, statistical NLP methods to modern, Transformer-based deep learning models.

---

## 💡 Core Concepts

### 1. Traditional NLP Pipeline
Traditional NLP relies on statistical approaches and manual text processing:
*   **Tokenization:** Splitting text into words, phrases, or symbols (tokens).
*   **Stopword Removal:** Eliminating common, low-information words like "the", "is", "at".
*   **Stemming & Lemmatization:** Reducing words to their root form (e.g., "running", "ran", "runs" $\rightarrow$ "run").
*   **Vectorization (TF-IDF):** Converting words to numerical vectors. 
    *   *Term Frequency (TF):* How frequent a word is in a document.
    *   *Inverse Document Frequency (IDF):* Penalizes words that appear across all documents (e.g., "said"), highlighting words unique to specific contexts.

### 2. The Transformer Revolution
Traditional architectures like RNNs and LSTMs read text sequentially (word-by-word), which makes it hard to parallelize and causes them to "forget" long-range context.

In 2017, the **Transformer** architecture introduced **Self-Attention**:
*   **Self-Attention:** Allows the model to look at other words in the input sequence to better understand the target word's context. For example, in *"The bank of the river"* vs. *"The bank account"*, the word "bank" attends to "river" or "account" to resolve its meaning.
*   **Pretraining & Fine-tuning:** Huge models (e.g., BERT, GPT) are pretrained on massive web data to understand grammar and facts. Developers then fine-tune them on small, labeled datasets for specific tasks.

---

## 🛠️ Python Implementation Files

1.  **`traditional_nlp.py`**: Tokenizes text, removes stopwords, and builds a TF-IDF vectorizer + Naive Bayes Classifier using Scikit-Learn to categorize text (e.g., tech vs. sports).
2.  **`transformer_sentiment.py`**: Uses the Hugging Face `transformers` library to load a pretrained transformer model (DistilBERT) and perform sentiment analysis (positive vs. negative classification) in just a few lines of code.
