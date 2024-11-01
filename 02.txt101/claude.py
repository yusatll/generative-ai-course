import anthropic  
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_key = os.getenv("claude_apikey")

client = anthropic.Anthropic(
    api_key=my_key
)

# Claude API kullanarak cevap oluşturma
# Generating a response using the Claude API
def generate_response(prompt):
    ai_response = client.messages.create(
        model="claude-2.1",
        temperature=0,
        max_tokens=256,
        messages=[
            {"role":"user", "content":prompt}
        ]
    )

    return ai_response.content[0].text


st.header("Claude kullanıyoruz") # Using Claude  
st.divider()

prompt = st.text_input("Mesaj gir") # Enter a message
submit_btn = st.button("Gönder") # Send

if submit_btn:
    response = generate_response(prompt)
    st.markdown(response)