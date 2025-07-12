import streamlit as st
from stt import listen
from translator import translate
from tts import speak

st.title("VoicePilot — Speech to Translation to Speech")

# Select target language
lang = st.selectbox("Choose target language:", options=["en", "es", "fr", "de", "zh-cn", "ja"])

if st.button("Start Listening"):
    text = listen()
    if text:
        st.write(f"Original: {text}")
        translated = translate(text, dest_lang=lang)
        st.write(f"Translated: {translated}")
        speak(translated, lang=lang)
    else:
        st.write("No speech detected.")
