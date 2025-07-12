from googletrans import Translator

translator = Translator()

def translate(text: str, dest_lang: str = "en") -> str:
    if not text:
        return ""
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""
