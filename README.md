# 🤖 Voice Interview Bot

A **voice-based AI interview bot** that can answer your questions in real-time.
This bot uses **Groq API** for Speech-to-Text (Whisper) and LLM (LLaMA) responses.
It supports both **terminal-based** and **Streamlit web UI** modes.

---

## **Features**

* 🎤 Voice input using microphone
* 📝 Speech-to-Text transcription via Groq Whisper
* 🤖 AI-generated interview-style answers via Groq LLaMA
* 🔊 Audio output using `pyttsx3`
* 🖥️ Optional Streamlit UI for browser interaction
* 💻 Lightweight on local machine (all heavy models run via Groq cloud)

---

## **Project Structure**

```
voice_interview_bot/
│── config.py        # API keys and model configuration
│── stt.py           # Speech-to-Text functions
│── llm.py           # LLM answer generation
│── tts.py           # Text-to-Speech
│── main.py          # Terminal-based bot
│── app.py           # Streamlit UI bot
│── requirements.txt # Python dependencies
```

---

## **Requirements**

Install dependencies using:

```bash
pip install -r requirements.txt
```

**Python packages:**

* `sounddevice`
* `numpy`
* `soundfile`
* `requests`
* `pyttsx3`
* `streamlit` (for web UI)

---

## **Setup**

1. Get your **Groq API Key** and replace it in `config.py`:

```python
GROQ_API_KEY = "your_groq_api_key_here"
```

2. Ensure your microphone works for recording.
3. For Streamlit UI, install `streamlit` if not already installed:

```bash
pip install streamlit
```

---

## **Usage**

### **1. Terminal Version**

Run the bot in terminal:

```bash
python main.py
```

* Speak your question.
* Bot transcribes your voice.
* Bot generates and speaks an answer.
* Continuous Q&A loop until you say **exit** or **quit**.

**Example Terminal Session:**

```
=== Voice Interview Bot ===
🎤 Speak now...
📝 You asked: What’s your superpower?
🤖 Bot Answer: My superpower is being a lifelong learner...
🎤 Speak now...
📝 You asked: exit
👋 Exiting Voice Interview Bot. Goodbye!
```

---

### **2. Streamlit Web UI**

Run the web UI:

```bash
streamlit run app.py
```

* Open the **Local URL** in your browser (e.g., [http://localhost:8501](http://localhost:8501))
* Click **🎤 Record Question**
* Speak your question
* View transcription and bot answer
* Hear audio playback

---

## **How it Works (Workflow)**

```
[User speaks question] 
        ↓
 [STT via Groq Whisper] 
        ↓
 [LLM via Groq LLaMA]
        ↓
[Answer displayed in terminal or Streamlit UI] + [Audio playback via pyttsx3]
```

---

## **Notes**

* Make sure your laptop has **microphone access**.
* All heavy AI computation happens on **Groq cloud**, so your laptop stays lightweight.
* Use **`exit` or `quit`** to stop the terminal bot.

