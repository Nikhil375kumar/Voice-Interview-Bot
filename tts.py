# tts.py - Text-to-Speech using pyttsx3 (lightweight, local)
import pyttsx3

def speak_text(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("=== Testing TTS ===")
    sample_text = "Hello, this is a test of the voice assistant system."
    print(f"Speaking: {sample_text}")
    speak_text(sample_text)
