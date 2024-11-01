import google.generativeai as genai
import PIL.Image
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
from io import BytesIO
from datetime import datetime

load_dotenv()

my_key = os.getenv("openai_apikey")

client = OpenAI(
    api_key=my_key
)

# OpenAI DALL-E ile görsel oluşturma fonksiyonu
# Function to generate an image with OpenAI DALL-E
def generate_image_with_dalle(prompt):

    ai_response = client.images.generate(
        model="dall-e-3",
        size="1024x1024", 
        quality="hd",
        n=1,
        response_format="url",
        prompt=prompt
    )

    image_url = ai_response.data[0].url

    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"./img/gen_image_{timestamp}.png"

    if not os.path.exists("./img"):
        os.makedirs("./img")

    with open(filename, "wb") as file:
        file.write(image_bytes.getbuffer())

    return filename


my_google_key = os.getenv("google_apikey")

genai.configure(
    api_key=my_google_key 
)

# Google Gemini Vision ile yerel bir resim kullanarak prompt oluşturma
# Generating a prompt using a local image with Google Gemini Vision
def gemini_vision_with_local_file(image_path, prompt):

    multimodality_prompt = f"""Bu gönderdiğim resmi, bazı ek yönergelerle birlikte yeniden oluşturmana istiyorum.
        Bunun için ilk olarak resmi son derece ayrıntılı biçimde betimle. Daha sonra sonucunda bana vereceğin metni, bir yapay zeka
        modelini kullanarak görsel oluşturmakta kullanacağım. O yüzden yanıtına son halini verirken bunun resim üretmekte kullanılacak bir
        girdi yani prompt olduğunu dikkate al. İşte ek yönerge şöyle: {prompt}
    """

    client = genai.GenerativeModel(model_name="gemini-pro-vision")

    source_image = PIL.Image.open(image_path)

    ai_response = client.generate_content(
        [
            multimodality_prompt,
            source_image  
        ]
    )

    ai_response.resolve()

    return ai_response.text

# Ana görsel oluşturma fonksiyonu
# Main image generation function  
def generate_image(img_path, prompt):
    img_based_prompt = gemini_vision_with_local_file(image_path=img_path, prompt=prompt)
    filename = generate_image_with_dalle(img_based_prompt)

    return filename