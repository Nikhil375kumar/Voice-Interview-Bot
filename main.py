# main.py - Continuous Q&A Voice Interview Bot
from stt import record_audio, transcribe_audio
from llm import generate_answer
from tts import speak_text

def main():
    print("=== Voice Interview Bot ===")
    print("Speak your question. Say 'exit' or 'quit' to stop.\n")

    while True:
        # Step 1: Record audio
        audio_data = record_audio()

        # Step 2: Transcribe using Groq Whisper
        question = transcribe_audio(audio_data)
        print(f"\n📝 You asked: {question}")

        # Check for exit condition
        if question.strip().lower() in ["exit", "quit"]:
            print("👋 Exiting Voice Interview Bot. Goodbye!")
            break

        # Step 3: Generate answer using Groq LLM
        answer = generate_answer(question)
        print(f"\n🤖 Bot Answer: {answer}")

        # Step 4: Speak the answer
        speak_text(answer)

if __name__ == "__main__":
    main()
