from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv("openai_api_key")

client = OpenAI(api_key=my_key)

# OpenAI API kullanarak cevap oluşturma
# Generating a response using the OpenAI API
ai_response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=256,
    messages=[
        {"role":"system", "content":"sen yardım sever bir asistansın"},
        {"role":"user", "content":"Mevsimler neden oluşur? dünya kendi etrafında döndüğü için mi?"}
    ]
)

# Cevabı ekrana yazdırma
# Printing the response
print(ai_response)
print(ai_response.choices[0].message.content)