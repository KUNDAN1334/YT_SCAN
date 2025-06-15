from groq import Groq
import os
import time
import tiktoken
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize tokenizer for counting tokens
encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text):
    """Count the number of tokens in a text string."""
    return len(encoding.encode(text))

def truncate_context(context, max_tokens=4000):
    """Truncate context to fit within token limits."""
    if count_tokens(context) <= max_tokens:
        return context
    
    # Split context into sentences and keep the most recent ones
    sentences = context.split('. ')
    truncated_context = ""
    
    # Start from the end and work backwards
    for sentence in reversed(sentences):
        test_context = sentence + ". " + truncated_context
        if count_tokens(test_context) > max_tokens:
            break
        truncated_context = test_context
    
    return truncated_context.strip()

def generate_answer(context, question):
    start_time = time.time()
    
    # Truncate context to fit within limits
    truncated_context = truncate_context(context, max_tokens=4000)
    
    prompt = f"""You are an AI assistant. Use the given context to answer the user's question.

Context:
{truncated_context}

Question:
{question}

Answer:"""
    
    # Check total prompt tokens
    prompt_tokens = count_tokens(prompt)
    print(f"Prompt tokens: {prompt_tokens}")
    
    if prompt_tokens > 5000:  # Leave room for response
        # Further truncate if still too large
        truncated_context = truncate_context(context, max_tokens=3000)
        prompt = f"""Context: {truncated_context}

Question: {question}

Answer:"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,  # Reasonable response length
            temperature=0.1,
            stream=False
        )
        
        end_time = time.time()
        print(f"Groq API response time: {end_time - start_time:.2f} seconds")
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response at this time."
