# config.py
# Store API keys and constants

GROQ_API_KEY = "your_groq_api_key_here"

# Models available on Groq
WHISPER_MODEL = "whisper-large-v3"   # for STT
LLM_MODEL = "llama-3.1-8b-instant"   # for interview answers

if __name__ == "__main__":
    print(" Config loaded successfully")
    print(f"Using Whisper model: {WHISPER_MODEL}")
    print(f"Using LLM model: {LLM_MODEL}")
