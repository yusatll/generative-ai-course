from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
my_key = os.getenv("openai_api_key")

client = OpenAI(api_key=my_key)

# Streamlit session state'inde mesajları saklama
# Storing messages in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [] # sohbet geçmişi / chat history
    st.session_state.messages.append({"role":"system", "content":"sen yardım sever bir asistansın"})

# Cevap oluşturma fonksiyonu
# Response generation function
def generate_response(prompt):
    st.session_state.messages.append({"role":"user", "content":prompt})

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    return ai_response.choices[0].message.content

st.header("İlk GPT botum") # My first GPT bot
st.divider()

# Sohbet geçmişini ekrana yazdırma
# Displaying the chat history
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan mesaj alma
# Getting input from the user  
if prompt := st.chat_input("Mesajınızı girin"): # Enter your message
    st.chat_message("user").markdown(prompt) # kullanıcının mesajını ekrana alıyoruz / displaying user's message

    response = generate_response(prompt)
    with st.chat_message("assistant"): # ikon kısmı / icon section
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant", "content":response})