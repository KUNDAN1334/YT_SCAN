import requests

def generate_answer(context, question):
    prompt = f"""You are an AI assistant. Use the given context to answer the user's question.

Context:
{context}

Question:
{question}

Answer:"""

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data['response'].strip()
