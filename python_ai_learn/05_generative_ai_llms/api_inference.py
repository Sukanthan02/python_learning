"""
Lesson 5.1: LLM API Inference (Gemini & OpenAI)
-----------------------------------------------
This script demonstrates how to call Commercial LLM APIs using official SDKs.
To ensure the script runs successfully even without API keys, we include
graceful checks and local mock simulations.
"""

import os

def demonstrate_gemini():
    print("=== 1. Google Gemini API Call ===")
    
    # Get API Key from environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("[No API Key found for Gemini. Simulating request/response...]")
        print("To run for real, set the env var: export GEMINI_API_KEY='your-key'\n")
        print("--- Code Example ---")
        code = """import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(
    "Explain quantum computing to a 10 year old.",
    generation_config=genai.types.GenerationConfig(
        temperature=0.7,
        max_output_tokens=150
    )
)
print(response.text)"""
        print(code)
        print("\n--- Simulated Gemini Output ---")
        print("Imagine computer bits are like light switches, either ON (1) or OFF (0).")
        print("A quantum computer uses 'qubits' which can be both ON and OFF at the same time!")
        print("This lets it solve super hard puzzles much faster than normal computers.")
        return

    # Real implementation if API key is present
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        # Using the standard fast model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("Sending prompt to Gemini...")
        response = model.generate_content("Explain machine learning in one sentence.")
        print(f"Gemini Response:\n{response.text}")
    except Exception as e:
        print(f"Error calling Gemini API: {e}")


def demonstrate_openai():
    print("\n=== 2. OpenAI API Call ===")
    
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("[No API Key found for OpenAI. Simulating request/response...]")
        print("To run for real, set the env var: export OPENAI_API_KEY='your-key'\n")
        print("--- Code Example ---")
        code = """from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a poetic assistant. Answer in rhymes."},
        {"role": "user", "content": "What is data science?"}
    ],
    temperature=0.5
)
print(response.choices[0].message.content)"""
        print(code)
        print("\n--- Simulated OpenAI Output ---")
        print("Data science is clean and bright,")
        print("Turning numbers into insight,")
        print("Finding patterns in the code,")
        print("To guide decisions down the road!")
        return

    # Real implementation if API key is present
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        print("Sending prompt to OpenAI...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Summarize what an API is in one sentence."}
            ]
        )
        print(f"OpenAI Response:\n{response.choices[0].message.content}")
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")


if __name__ == "__main__":
    demonstrate_gemini()
    demonstrate_openai()
