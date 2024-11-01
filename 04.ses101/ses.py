from openai import OpenAI
import assemblyai as aai
import streamlit as st
import os
from dotenv import load_dotenv

# Çevre değişkenlerini yükle / Load environment variables
load_dotenv()

# API anahtarlarını al / Get API keys
openai_key = os.getenv("chatgpt_apikey")
aai_key = os.getenv("assemblyai_apikey")

# OpenAI istemcisini oluştur / Create OpenAI client
client = OpenAI(
    api_key=openai_key
)

# Metinden ses oluşturma fonksiyonu / Text-to-speech function
def create_speech_from_text(prompt, speech_file, voice_type):
    ai_response = client.audio.speech.create(
        model="tts-1",
        voice=voice_type,
        response_format="mp3",
        input=prompt
    )

    ai_response.stream_to_file(speech_file)
    return True

# Whisper modeli ile ses dosyasını metne dönüştürme / Transcribe audio file using Whisper model
def transcribe_whisper(audio_filename):
    audio_file = open(audio_filename, "rb")

    ai_transkript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="en"
    )

    return ai_transkript.text

# Whisper modeli ile ses dosyasını tercüme etme / Translate audio file using Whisper model
def translate_whisper(audio_filename):
    audio_file = open(audio_filename, "rb")

    ai_translation = client.audio.translations.create(
        model="whisper-1",
        file=audio_file
    )

    return ai_translation.text

# AssemblyAI Conformer modeli ile ses dosyasını metne dönüştürme / Transcribe audio file using AssemblyAI Conformer model
def transcribe_conformer(audio_filename):
    aai.settings.api_key = aai_key
    transcriber = aai.Transcriber()
    generated = transcriber.transcribe(data=audio_filename)

    return generated.text

# Streamlit kullanıcı arayüzü / Streamlit user interface
tab_tts, tab_whisper, tab_translation, tab_conformer = st.tabs(
    [
        "TTS ses sentezleme",
        "Whisper transkripsion",
        "Whisper Tercüme",
        "Conformer Transkripsion"
    ]
)

# TTS ses sentezleme sekmesi / TTS (Text-to-Speech) tab
with tab_tts:
    st.subheader("TTS ses sentezleme")
    st.divider()

    prompt = st.text_input("seslendirilecek metni girin", key="prompt_tts")
    voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    voice_type = st.selectbox(label="Ses tercihiniz", options=voices, key="voice_tts")
    generate_btn = st.button("Gonder", key="btn_tts")

    if generate_btn:
        status = create_speech_from_text(prompt, "speechfile.mp3", voice_type)
        st.success(status)

        audio_file = open("speechfile.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(data=audio_bytes, format="audio/mp3")

# Whisper transkripsiyon sekmesi / Whisper transcription tab
with tab_whisper:
    st.subheader("Whisper transkripsion")
    st.divider()

    selected_file = st.file_uploader("Ses dosyası", type=["wav"], key="file_Whisper")
    if selected_file:
        audio_file = open(selected_file.name, "rb")
        audio_bytes = audio_file.read()
        st.audio(data=audio_bytes, format="audio/mp3")

    transcribe_btn = st.button("Metne dönüştür", key="btn_whisper")

    if transcribe_btn:
        generated = transcribe_whisper(selected_file.name)
        st.divider()

        st.info(f"Transkripsion: {generated}")
        st.balloons()

# Whisper tercüme sekmesi / Whisper translation tab
with tab_translation:
    st.subheader("Whisper Tercüme")
    st.divider()

    selected_file = st.file_uploader("Ses dosyası", type=["mp3"], key="file_translation")
    if selected_file:
        audio_file = open(selected_file.name, "rb")
        audio_bytes = audio_file.read()
        st.audio(data=audio_bytes, format="audio/mp3")

    translate_btn = st.button("Tercüme et", key="btn_translation")

    if translate_btn:
        translated = translate_whisper(selected_file)
        st.divider()

        st.info(f"Translation: {translated}")
        st.balloons()

# Conformer transkripsiyon sekmesi / Conformer transcription tab
with tab_conformer:
    st.subheader("Conformer transkripsion")
    st.divider()

    selected_file = st.file_uploader("Ses dosyası", type=["wav"], key="file_conformer")
    if selected_file:
        audio_file = open(selected_file.name, "rb")
        audio_bytes = audio_file.read()
        st.audio(data=audio_bytes, format="audio/mp3")

    transcribe_btn = st.button("Metne dönüştür", key="btn_conformer")

    if transcribe_btn:
        generated = transcribe_conformer(selected_file.name)
        st.divider()

        st.info(f"Transkripsion: {generated}")
        st.balloons()