import streamlit as st
import threading
import recorder, transcriptor, painter

# Streamlit session state değişkenleri
# Streamlit session state variables
if "record_active" not in st.session_state:
    st.session_state.record_active = threading.Event()
    st.session_state.recording_status = "Başlamaya Hazırız!" # Ready to start!
    st.session_state.recording_completed = False
    st.session_state.latest_image = ""
    st.session_state.messages = []
    st.session_state.frames = []

# Ses kaydını başlatan fonksiyon 
# Function to start the voice recording
def start_recording():
    st.session_state.record_active.set() # thread i set et / set the thread
    st.session_state.frames = [] # yeniden başlatmak için sıfırladık / reset to restart
    st.session_state.recording_status = "** Sesiniz Kaydediliyor...**" # Your voice is being recorded...
    st.session_state.recording_completed = False

    threading.Thread(target=recorder.record, args=(st.session_state.record_active, st.session_state.frames)).start()

# Ses kaydını durduran fonksiyon
# Function to stop the voice recording  
def stop_recording():
    st.session_state.record_active.clear() 
    st.session_state.recording_status = "**Kayıt Tamamlandı! **" # Recording completed!
    st.session_state.recording_completed = True

# Streamlit sayfa ayarları 
# Streamlit page configuration
st.set_page_config(page_title="VoiceDraw", layout="wide", page_icon="./icons/app_icon.png")
st.image(image="./icons/banner.png", use_column_width=True)
st.title("VoiceDraw: Sesli Çizim") # VoiceDraw: Voice Drawing
st.divider()

col_audio, col_img = st.columns([1,4])

with col_audio:
    st.subheader("Ses kayıt") # Voice recording
    st.divider()

    status_message = st.info(st.session_state.recording_status)
    st.divider()

    subcol_left, subcol_right = st.columns([1,2])

    with subcol_left:
        start_btn = st.button(label="Başlat", on_click=start_recording, disabled=st.session_state.record_active.is_set()) # Start
        stop_btn = st.button(label="Durdur", on_click=stop_recording, disabled=not st.session_state.record_active.is_set()) # Stop

    with subcol_right:
        recorded_audio = st.empty()

        if st.session_state.recording_completed:
            recorded_audio.audio(data="voice_prompt.wav")

    st.divider()
    latest_image_use = st.checkbox(label="Son Resmi Kullan") # Use latest image

with col_img:
    st.subheader("Görsel Çıktılar") # Visual Outputs 
    st.divider()

    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message(name=message["role"], avatar="./icons/ai_avatar.png"):
                st.warning("İşte sizin için oluşturduğum görsel:") # Here is the visual I created for you:
                st.image(image=message["content"], width=300)
            
        elif message["role"] == "user":
            with st.chat_message(name=message["role"], avatar="./icons/user_avatar.png"):
                st.success(message["content"])

    if stop_btn:
        with st.chat_message(name="user", avatar="./icons/user_avatar.png"):
            with st.spinner("Sesiniz çözümleniyor..."): # Your voice is being transcribed...
                voice_prompt = transcriptor.transcribe_with_whisper(audio_filename="voice_prompt.wav")
            st.success(voice_prompt)

        st.session_state.messages.append({"role":"user", "content": voice_prompt})

        with st.chat_message(name="assistant", avatar="./icons/ai_avatar.png"):
            st.warning("İşte sizin için oluşturduğum görsel:") # Here is the visual I created for you: 

            with st.spinner("Görsel oluşturuluyor..."): # Visual is being created...
                if latest_image_use:
                    image_filename = painter.generate_image(img_path=st.session_state.latest_image, prompt=voice_prompt)
                else:
                    image_filename = painter.generate_image_with_dalle(prompt=voice_prompt)

            st.image(image=image_filename, width=300)

            with open(image_filename, "rb") as file:
                st.download_button(
                    label="Resmi indir", # Download the image
                    data=file,
                    file_name=image_filename,
                    mime="image/png"
                )
        
        st.session_state.messages.append({"role":"assistant", "content": image_filename})
        st.session_state.latest_image = image_filename