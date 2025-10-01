# app.py - Streamlit UI for Voice Interview Bot
import streamlit as st
from stt import record_audio, transcribe_audio
from llm import generate_answer
from tts import speak_text
import tempfile
import soundfile as sf

st.set_page_config(page_title="Voice Interview Bot", page_icon="🤖")

st.title("🤖 Voice Interview Bot")
st.write("Ask questions via voice and get interview-style answers from the bot.")

# Button to start recording
if st.button("🎤 Record Question"):
    st.info("Listening... Speak now (Stops after silence)")

    # Step 1: Record Audio
    audio_data = record_audio()

    # Step 2: Transcribe Audio
    st.info("Transcribing...")
    question = transcribe_audio(audio_data)
    st.write("**You asked:**", question)

    # Step 3: Generate Answer via LLM
    st.info("Generating answer...")
    answer = generate_answer(question)
    st.write("**Bot Answer:**", answer)

    # Step 4: Play Audio Response
    st.info("Playing audio answer...")
    # Save TTS to temporary WAV
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio_data, 16000)  # Optional: dummy audio if TTS not saving
        speak_text(answer)  # Speak using pyttsx3 (or you can integrate TTS engine to save audio)
        st.audio(f.name)

st.markdown("---")
st.write("💡 Tip: Click the button, ask your question, wait for answer and audio playback.")
