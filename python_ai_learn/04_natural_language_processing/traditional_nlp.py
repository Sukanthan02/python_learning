"""
Lesson 4.1: Traditional NLP & Text Classification
---------------------------------------------------
This script demonstrates how to preprocess text data (tokenization, cleaning)
and convert it into numerical representations using TF-IDF (Term Frequency-
Inverse Document Frequency). We then train a Naive Bayes classifier on it.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# 1. Custom Text Preprocessing Function (Manual tokenization & stopword cleaning)
# Using manual implementation so it is light, fast, and does not require nltk downloads.
def clean_and_tokenize(text):
    # Standard English stopwords list
    stopwords = {"the", "is", "at", "which", "on", "a", "an", "and", "but", "to", "for", "with", "in", "of", "this", "that"}
    
    # Lowercase and clean punctuation
    cleaned_text = "".join([char.lower() if char.isalnum() or char.isspace() else " " for char in text])
    
    # Tokenize (split by space)
    tokens = cleaned_text.split()
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stopwords]
    
    return " ".join(filtered_tokens)


def run_traditional_nlp():
    print("=== Traditional NLP: TF-IDF Text Classification ===")
    
    # Synthetic dataset: Short sentences labeled as 0 (Technology) or 1 (Sports)
    corpus = [
        "The new smartphone has a fast processor and high resolution screen.",
        "Our team won the championship match in the final minutes.",
        "Apple announced a new laptop with long battery life.",
        "The football player scored a historic goal in yesterday's game.",
        "Artificial intelligence is changing the software development industry.",
        "The tennis player won three grand slam tournaments in a row.",
        "Cloud database services offer scalable storage solutions.",
        "Basketball practice was intensive before the league final tournament."
    ]
    
    # Labels: 0 = Tech, 1 = Sports
    labels = [0, 1, 0, 1, 0, 1, 0, 1]
    
    # 2. Preprocess the Corpus
    print("\nOriginal Text Sample:\n", corpus[0])
    cleaned_corpus = [clean_and_tokenize(doc) for doc in corpus]
    print("\nPreprocessed Text Sample:\n", cleaned_corpus[0])
    
    # 3. TF-IDF Vectorization
    # Converts text documents to a matrix of TF-IDF features.
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(cleaned_corpus)
    
    # Inspect feature vocabulary
    print("\nVocabulary mapped to columns:")
    print(vectorizer.vocabulary_)
    print(f"Feature matrix shape: {X.toarray().shape} (8 documents, unique words)")
    
    # 4. Train Naive Bayes Classifier on full dataset (since it is a tiny demo dataset)
    # Multinomial Naive Bayes is highly effective for text data word counts/TF-IDF
    clf = MultinomialNB()
    clf.fit(X, labels)
    
    # 5. Evaluate on Training Data
    y_pred = clf.predict(X)
    print("\n--- Model Evaluation (On Training Data) ---")
    print(f"Accuracy: {accuracy_score(labels, y_pred) * 100:.1f}%")
    print("\nClassification Report:")
    print(classification_report(labels, y_pred, target_names=["Tech", "Sports"]))
    
    # Test on a new phrase
    new_phrase = "I love playing basketball and scoring points."
    cleaned_new = clean_and_tokenize(new_phrase)
    vectorized_new = vectorizer.transform([cleaned_new])
    prediction = clf.predict(vectorized_new)[0]
    category = "Sports" if prediction == 1 else "Tech"
    print(f"\nNew Sentence: '{new_phrase}'\nPredicted Class: {category} (Correct answer should be Sports)")

if __name__ == "__main__":
    run_traditional_nlp()
