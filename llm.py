# llm.py - Generate interview answers using Groq LLM
import requests
from config import GROQ_API_KEY, LLM_MODEL

def generate_answer(question: str):
    system_prompt = (
        "You are Nikhil Kumar, interviewing for an AI Agent role at 100x. "
        "Answer questions in first person, confident, professional, concise. "
        "Highlight strengths, superpower, growth mindset, and adaptability."
    )

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
        json={
            "model": LLM_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        },
    )

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("=== Testing LLM ===")
    sample_question = "What’s your #1 superpower?"
    answer = generate_answer(sample_question)
    print(f"Q: {sample_question}")
    print(f"A: {answer}")
