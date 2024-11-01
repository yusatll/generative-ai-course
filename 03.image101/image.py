from openai import OpenAI
import streamlit as st
import requests
from io import BytesIO
import base64
import os
from dotenv import load_dotenv

# Çevre değişkenlerini yükle / Load environment variables
load_dotenv()

# API anahtarlarını al / Get API keys
openai_key = os.getenv("chatgpt_apikey")
stability_key = os.getenv("stabilityai_apikey")

# OpenAI istemcisini oluştur / Create OpenAI client
client = OpenAI(
    api_key=openai_key
)

# DALL-E 3 ile görsel oluşturma / Image generation with DALL-E 3
def generate_image(prompt):
    ai_response = client.images.generate(
        model="dall-e-3",
        size="1024x1024",
        quality="hd",
        n=1,
        response_format="url",
        prompt=prompt
    )
    image_url = ai_response.data[0].url
    revised_prompt = ai_response.data[0].revised_prompt

    # Görsel URL'sinden byte verisi al / Get byte data from image URL
    response = requests.get(image_url)
    img_bytes = BytesIO(response.content)

    return img_bytes, revised_prompt

# DALL-E 3 ile varyasyon oluşturma / Create variation with DALL-E 3
def create_variation(source_img_url):
    ai_response = client.images.create_variation(
        image=open(source_img_url, "rb"),
        size="1024x1024",
        n=1,
        response_format="url"
    )

    generated_img_url = ai_response.data[0].url
    response = requests.get(generated_img_url)
    img_bytes = BytesIO(response.content)

    return img_bytes

# Stable Diffusion ile görsel oluşturma / Image generation with Stable Diffusion
def generate_stable_diffisuon(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"

    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data",
        "authorization": f"Bearer {stability_key}",
        "boundary": "blurry"
    }

    # body = {
    #     "steps": 40,
    #     "width": 1024,
    #     "height": 1024,
    #     "seed": 0,
    #     "cfg_scale": 5,
    #     "samples": 1,
    #     "text_prompts": [
    #         {
    #             "text": prompt,
    #             "weight": 1
    #         },
    #         {
    #             "text": "blurry, bad",
    #             "weight": -1
    #         }
    #     ],
    # }

    body = {
        "prompt": prompt,
        "output_format": "webp",
    }
    response = requests.post(url=url, headers=headers, json=body, files={"none": ''})
    data = response.json()
    return response

# Streamlit kullanıcı arayüzü / Streamlit user interface
tab_generate, tab_variation, tab_sd = st.tabs(["Resim Üret", "Varyasyon Oluştur", "Stable Diffusion"])

# DALL-E 3 görsel oluşturma sekmesi / DALL-E 3 image generation tab
with tab_generate:
    st.subheader("DALL-E 3 ile görsel oluşturma")
    st.divider()
    prompt = st.text_input("Görseli tanımla")
    generate_btn = st.button("Oluştur")

    if generate_btn:
        img_data, revised = generate_image(prompt)
        st.image(image=img_data)
        st.divider()
        st.caption(revised)

# DALL-E 3 varyasyon oluşturma sekmesi / DALL-E 3 variation creation tab
with tab_variation:
    st.subheader("DALL-E 3 ile Vasyasyon oluşturma")
    st.divider()
    selected_file = st.file_uploader("PNG formatında görsel yükle", type=["png"])
    
    if selected_file:
        st.image(image=selected_file.name)

    variation_btn = st.button("Varyasyon Oluştur")

    if variation_btn:
        img_data = create_variation(selected_file.name)
        st.image(image=img_data)

# Stable Diffusion görsel oluşturma sekmesi / Stable Diffusion image generation tab
with tab_sd:
    st.subheader("Stable Diffusion ile görsel oluşturma")
    st.divider()
    prompt_sd = st.text_input("Görseli tanımla", key="sd_text_input")
    generate_btn_sd = st.button("Oluştur", key="sd_btn")

    if generate_btn_sd:
        data = generate_stable_diffisuon(prompt_sd)
        print("status_code", data.status_code)
        print("data",data)
        if data.status_code == 200:
            with open("./lighthouse.webp", 'wb') as file:
                file.write(data.content)
        else:
            raise Exception(str(data.json()))
        # for img in data["artifacts"]:
        #     img_bytes = base64.b64decode(img["base64"])
        #     st.image(image=img_bytes)
