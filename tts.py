from gtts import gTTS
import os
import tempfile

def speak(text: str, lang: str = "en"):
    if not text:
        print("No text to speak.")
        return
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            os.system(f"afplay {fp.name}")  # Mac's default audio player
    except Exception as e:
        print(f"TTS error: {e}")
