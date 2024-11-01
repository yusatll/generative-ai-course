import cohere
import os  
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_key = os.getenv("cohere_apikey")

client = cohere.Client(
    api_key=my_key
)

# Cohere API kullanarak cevap oluşturma
# Generating a response using the Cohere API
def generate_response(prompt):
    ai_response = client.chat(
        model="command",
        temperature=0,
        max_tokens=256,
        chat_history=[
            {"role":"USER", "message":"yer çekimini kim bulmuştur?"},
            {"role":"CHATBOT", "message":"çekim yasalarını bulan Newton."}
        ],
        message=prompt
    )

    return ai_response.text

st.header("Cohere kullanıyoruz") # Using Cohere
st.divider()

prompt = st.text_input("Mesaj gir") # Enter a message  
submit_btn = st.button("Gönder") # Send

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)