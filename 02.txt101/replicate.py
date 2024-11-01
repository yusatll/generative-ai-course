import replicate 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


prompt = "mevsimler nasıl oluşur?" # How do seasons form?
system_prompt = "Sen yardımsever bir asistansın." # You are a helpful assistant.

# Llama 2 modeli kullanarak cevap oluşturma ve çıktıyı akışlı olarak alma
# Generating a response using the Llama 2 model and streaming the output
for event in replicate.stream(
    "meta/llama-2-70b-chat",
    input={
        "top_k": 0,
        "top_p": 1,
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.5,
        "system_prompt": system_prompt,
        "length_penalty": 1,
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        "prompt_template": "<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
        "presence_penalty": 0,
        "log_performance_metrics": False
    },
):
    print(str(event), end="")

print("-"*50)

# Mistral modeli kullanarak cevap oluşturma ve çıktıyı akışlı olarak alma
# Generating a response using the Mistral model and streaming the output  
for event in replicate.stream(
    "mistralai/mixtral-8x7b-instruct-v0.1",
    input={
        "top_k": 50,
        "top_p": 0.9,
        "prompt": prompt,
        "temperature": 0.6,
        "system_prompt": system_prompt,
        "length_penalty": 1,
        "max_new_tokens": 1024,
        "prompt_template": "<s>[INST] {prompt} [/INST] ",
        "presence_penalty": 0
    },
):
    print(str(event), end="")