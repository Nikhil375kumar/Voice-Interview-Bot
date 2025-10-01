# stt.py - Speech-to-Text using Groq Whisper
import sounddevice as sd
import numpy as np
import time
import requests
import io
import soundfile as sf
from config import GROQ_API_KEY, WHISPER_MODEL

SAMPLE_RATE = 16000
SILENCE_THRESHOLD = 0.01
SILENCE_DURATION = 3

def record_audio():
    print("🎤 Speak now... (Stops when silent for 2s)")
    audio_buffer = []
    silence_start = None
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype=np.float32)

    with stream:
        while True:
            audio_chunk, _ = stream.read(int(SAMPLE_RATE * 0.1))
            audio_buffer.append(audio_chunk)

            volume = np.max(np.abs(audio_chunk))
            if volume < SILENCE_THRESHOLD:
                if silence_start is None:
                    silence_start = time.time()
                elif time.time() - silence_start >= SILENCE_DURATION:
                    break
            else:
                silence_start = None

    recorded_audio = np.concatenate(audio_buffer, axis=0).flatten()
    return recorded_audio

def transcribe_audio(audio_data):
    print("⏳ Sending audio to Groq Whisper...")
    
    # Save as temporary WAV
    with io.BytesIO() as wav_buffer:
        sf.write(wav_buffer, audio_data, SAMPLE_RATE, format="WAV")
        wav_buffer.seek(0)

        response = requests.post(
            "https://api.groq.com/openai/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            files={"file": ("audio.wav", wav_buffer, "audio/wav")},
            data={"model": WHISPER_MODEL},
        )
    
    transcription = response.json().get("text", "")
    return transcription

if __name__ == "__main__":
    print("=== Testing STT ===")
    audio = record_audio()
    text = transcribe_audio(audio)
    print(f"📝 Transcribed text: {text}")
