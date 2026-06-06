"""
Lesson 5.2: Retrieval-Augmented Generation (RAG) from Scratch
-------------------------------------------------------------
This script demonstrates the complete RAG pipeline:
1. Document Ingestion (creating a local knowledge base)
2. Text Chunking & Vectorization (using TF-IDF as a local embedding model)
3. Semantic Search (using Cosine Similarity to find relevant passages)
4. Prompt Augmentation (injecting search results into the LLM context)
5. Generation (Simulating final LLM completion)
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Knowledge Base (Internal Company Documents)
documents = [
    "Company Work Hours Policy: Our core operating hours are Monday through Friday, 9:00 AM to 5:00 PM EST. Flexible schedules are allowed with manager approval.",
    "Health Insurance Benefits: Comprehensive medical, dental, and vision insurance options are available to all full-time employees starting their first day.",
    "Annual Leave Guidelines: Employees receive 20 days of paid time off (PTO) per year, which accrues monthly. Unused PTO can carry over up to a maximum of 5 days.",
    "Remote Work Agreement: Employees can work remotely up to 3 days per week. Equipment such as monitors, laptops, and keyboards are reimbursed up to $500.",
    "Referral Program Bonus: If you refer a candidate who is hired and stays for at least 6 months, you will receive a cash bonus of $2,000 on your next paycheck."
]

def run_rag_pipeline(query):
    print(f"\n=========================================")
    print(f"USER QUERY: '{query}'")
    print(f"=========================================")
    
    # 2. Vectorization (Embedding Simulation)
    # TfidfVectorizer converts text into numerical vectors that represent semantic importance of words.
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the documents into vector embeddings
    doc_embeddings = vectorizer.fit_transform(documents)
    
    # Convert query into the same vector space
    query_embedding = vectorizer.transform([query])
    
    # 3. Retrieve (Semantic Search via Cosine Similarity)
    # Cosine similarity measures the angle between vectors (values close to 1.0 mean highly similar)
    similarities = cosine_similarity(query_embedding, doc_embeddings).flatten()
    
    # Find the document index with the highest similarity score
    best_match_idx = np.argmax(similarities)
    best_score = similarities[best_match_idx]
    
    retrieved_context = documents[best_match_idx]
    
    print("\n--- Step 1: Retrieval (Semantic Search) ---")
    print("Similarity Scores for each document:")
    for idx, score in enumerate(similarities):
        print(f"  Doc {idx+1}: Score = {score:.4f} | '{documents[idx][:40]}...'")
        
    print(f"\nTop Match: Doc {best_match_idx+1} with score {best_score:.4f}")
    print(f"Retrieved Context: \"{retrieved_context}\"")
    
    # 4. Augment (Construct Prompt with Context)
    # We combine the retrieved knowledge with the user's query into a single template.
    prompt_template = f"""
Answer the user query based ONLY on the provided Context. If the context does not contain the answer, say "I don't know".

Context:
{retrieved_context}

User Query: {query}
Answer:
"""
    print("\n--- Step 2: Prompt Augmentation ---")
    print("Augmented Prompt prepared for the LLM:")
    print(prompt_template.strip())
    
    # 5. Generate (Simulate LLM Output)
    print("\n--- Step 3: Generation (LLM Response) ---")
    # In a production app, you would send prompt_template to OpenAI/Gemini:
    # response = openai_client.chat.completions.create(..., messages=[{"role": "user", "content": prompt_template}])
    
    # We will simulate the response based on which document was matched
    if best_score < 0.25:
        llm_response = "I do not have enough information in my knowledge base to answer that query."
    elif best_match_idx == 0:
        llm_response = "According to our work hours policy, the core hours are Monday through Friday, 9:00 AM to 5:00 PM EST, though flexible schedules are possible with manager approval."
    elif best_match_idx == 1:
        llm_response = "Full-time employees are eligible for medical, dental, and vision insurance starting on their very first day."
    elif best_match_idx == 2:
        llm_response = "You receive 20 days of PTO per year. You can carry over a maximum of 5 unused days into the next year."
    elif best_match_idx == 3:
        llm_response = "You are permitted to work remotely up to 3 days each week, and the company reimburses work-from-home equipment up to $500."
    elif best_match_idx == 4:
        llm_response = "If you refer a candidate who gets hired and remains with the company for at least 6 months, you will receive a referral bonus of $2,000."
        
    print(f"LLM Output:\n{llm_response}")


if __name__ == "__main__":
    # Test case A: Query related to office hours
    run_rag_pipeline("What are the office hours and is there flexibility?")
    
    # Test case B: Query related to remote working equipment
    run_rag_pipeline("How much money can I get reimbursed for remote work monitors?")
    
    # Test case C: Query about something outside the documents
    run_rag_pipeline("What is the company dress code policy?")
