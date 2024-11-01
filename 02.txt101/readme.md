# AI Chatbot Örnekleri / AI Chatbot Examples

Bu proje, farklı yapay zeka API'lerini kullanarak chatbot uygulamaları oluşturmayı gösterir. Projede OpenAI, Anthropic, Cohere ve Google Generative AI API'leri kullanılmıştır. Her bir API için ayrı bir örnek dosya bulunmaktadır.

This project demonstrates how to create chatbot applications using different artificial intelligence APIs. The project utilizes OpenAI, Anthropic, Cohere, and Google Generative AI APIs. There is a separate example file for each API.

## Özellikler / Features

- OpenAI API ile chatbot oluşturma / Creating a chatbot with OpenAI API
- Anthropic Claude API ile chatbot oluşturma / Creating a chatbot with Anthropic Claude API
- Cohere Command API ile chatbot oluşturma / Creating a chatbot with Cohere Command API
- Google Generative AI (Gemini) API ile chatbot oluşturma / Creating a chatbot with Google Generative AI (Gemini) API
- Streamlit kullanarak interaktif web uygulamaları oluşturma / Creating interactive web applications using Streamlit

## Gereksinimler / Requirements

- Python 3.7+
- OpenAI API anahtarı / OpenAI API key
- Anthropic API anahtarı / Anthropic API key
- Cohere API anahtarı / Cohere API key
- Google Generative AI API anahtarı / Google Generative AI API key
- Streamlit

## Kurulum / Setup

1. Repo'yu klonlayın / Clone the repo
    ```
    git clone https://github.com/yourusername/ai-chatbot-examples.git
    ```

2. Gerekli kütüphaneleri yükleyin / Install the required libraries
    ```
    pip install -r requirements.txt
    ```

3. `.env` dosyasını oluşturun ve API anahtarlarınızı ekleyin / Create a `.env` file and add your API keys
    ```
    openai_api_key=YOUR_OPENAI_API_KEY
    claude_apikey=YOUR_ANTHROPIC_API_KEY
    cohere_apikey=YOUR_COHERE_API_KEY
    google_apikey=YOUR_GOOGLE_API_KEY
    ```

## Kullanım / Usage

Her bir örnek dosyayı ayrı ayrı çalıştırabilirsiniz:
You can run each example file separately:

- OpenAI örneği / OpenAI example: `streamlit run chat.py`
- Anthropic Claude örneği / Anthropic Claude example: `streamlit run claude.py`
- Cohere Command örneği / Cohere Command example: `streamlit run command.py`
- Google Generative AI (Gemini) örneği / Google Generative AI (Gemini) example: `streamlit run gemini.py`

## Lisans / License

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

This project is licensed under the MIT License. See the `LICENSE` file for more information.