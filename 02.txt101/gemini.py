import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_key = os.getenv("google_apikey")

genai.configure(
    api_key=my_key
)

client = genai.GenerativeModel(
    model_name="gemini-pro",
)

# Gemini API kullanarak cevap oluşturma
# Generating a response using the Gemini API  
def generate_response(prompt):
    chat = client.start_chat(history=[])

    ai_response = chat.send_message(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=0,
            max_output_tokens=256
        )
    )

    return ai_response.text


st.header("Gemini kullanıyoruz") # Using Gemini
st.divider()

prompt = st.text_input("Mesaj gir") # Enter a message
submit_btn = st.button("Gönder") # Send

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)


# ai_response = client.generate_content(
#     "mevsimler neden oluşur?",
#     generation_config=genai.GenerationConfig(
#         temperature=0,
#         max_output_tokens=256
#     )
# )

# print(ai_response.text)

