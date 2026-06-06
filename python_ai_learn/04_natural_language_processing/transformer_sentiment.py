"""
Lesson 4.2: Transformer-based NLP with Hugging Face
---------------------------------------------------
This script demonstrates how to perform Sentiment Analysis using the Hugging 
Face library. It illustrates both:
1. The simple high-level 'pipeline' API.
2. The low-level Tokenizer & Model combination (explaining how transformer outputs work).

Includes an offline mock fallback in case model download fails or is too slow.
"""

import torch
import torch.nn.functional as F

def run_low_level_transformer(text, tokenizer, model):
    """
    Demonstrates what happens under the hood of a pipeline.
    """
    print("\n--- Under the Hood: Tokenizer & Model Analysis ---")
    
    # 1. Tokenize Text
    # Returns input IDs, token type IDs, and attention masks as PyTorch Tensors
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    print("Tokenized Inputs:")
    for key, val in inputs.items():
        print(f"  {key}: {val.shape} -> {val[0]}")
        
    # 2. Forward Pass through Model
    with torch.no_grad():
        outputs = model(**inputs)
        
    # 3. Obtain logits (raw output values from classification head)
    logits = outputs.logits
    print(f"\nModel Raw Outputs (Logits): {logits}")
    
    # 4. Convert logits to probabilities using Softmax
    probabilities = F.softmax(logits, dim=-1)
    print(f"Calculated Probabilities: {probabilities}")
    
    # 5. Extract label mapping
    pred_class_idx = torch.argmax(probabilities).item()
    confidence = probabilities[0][pred_class_idx].item()
    label = model.config.id2label[pred_class_idx]
    
    print(f"Prediction: {label} (Confidence: {confidence:.2%})")


def run_pipeline_sentiment():
    print("=== Modern NLP: Hugging Face Transformers ===")
    
    sample_text = "I absolutely love learning about artificial intelligence! It is amazing."
    print(f"Input Sentence: '{sample_text}'")
    
    try:
        from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
        
        # Load pre-trained sentiment analysis model
        # By default, this uses DistilBERT-SST-2-English
        print("\nLoading pretrained transformer (DistilBERT)...")
        sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        
        # Run inference
        result = sentiment_pipeline(sample_text)[0]
        print("\n--- Pipeline Sentiment Analysis ---")
        print(f"Label:      {result['label']}")
        print(f"Confidence: {result['score']:.2%}")
        
        # Load components manually to demonstrate the low-level API
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        run_low_level_transformer(sample_text, tokenizer, model)
        
    except Exception as e:
        print(f"\n[Note/Warning] Pre-trained model loading failed or skipped. Error: {e}")
        print("This typically happens offline or if package installations are missing.")
        print("\n--- Simulating Transformer outputs for education ---")
        print("If the model loaded successfully, it would return:")
        print("  Label: POSITIVE")
        print("  Confidence: 99.98%")
        print("\nUnder the hood process explanation:")
        print("  1. The string is split into wordpieces (e.g. ['i', 'absolutely', 'love', 'learn', '##ing'])")
        # Show mock input IDs
        print("  2. Wordpieces are mapped to vocabulary indices: input_ids = Tensor([101, 1045, 9054, ...])")
        print("  3. The model returns logits (raw confidence scores): logits = Tensor([[-4.1, 4.3]])")
        print("  4. Softmax activation normalizes logits to probabilities: [0.0002, 0.9998]")

if __name__ == "__main__":
    run_pipeline_sentiment()
