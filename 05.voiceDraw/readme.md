# VoiceDraw: Sesli Çizim / VoiceDraw: Voice Drawing

VoiceDraw, kullanıcının sesli komutlarını alarak yapay zeka tarafından görsel çıktılar oluşturan bir uygulamadır. Uygulama, OpenAI DALL-E ve Google Gemini Vision modelleri kullanarak, sesli komutlardan görseller üretir.

VoiceDraw is an application that takes voice commands from the user and generates visual outputs using artificial intelligence. The application uses OpenAI DALL-E and Google Gemini Vision models to generate visuals from voice commands.

## Özellikler / Features

- Sesli komut ile görsel oluşturma / Generating visuals with voice commands
- Oluşturulan görsellerin görüntülenmesi ve indirilmesi / Viewing and downloading the generated visuals
- Önceki görseli referans alarak yeni görsel oluşturma / Generating new visuals based on the previous visual as reference
- Türkçe ve İngilizce dil desteği / Turkish and English language support

## Gereksinimler / Requirements

- Python 3.7+
- Streamlit
- PyAudio
- OpenAI API anahtarı / OpenAI API key
- Google Generative AI API anahtarı / Google Generative AI API key

## Kurulum / Setup

1. Repo'yu klonlayın / Clone the repo
    ```
    git clone https://github.com/yourusername/voicedraw.git
    ```

2. Gerekli kütüphaneleri yükleyin / Install the required libraries
    ```
    pip install -r requirements.txt
    ```

3. `.env` dosyasını oluşturun ve API anahtarlarınızı ekleyin / Create a `.env` file and add your API keys
    ```
    openai_apikey=YOUR_OPENAI_API_KEY
    google_apikey=YOUR_GOOGLE_API_KEY
    ```

4. Uygulamayı çalıştırın / Run the application
    ```
    streamlit run app.py
    ```

## Kullanım / Usage

1. Uygulamayı başlatın ve "Başlat" düğmesine tıklayın / Launch the application and click the "Start" button
2. Sesli komutunuzu verin ve "Durdur" düğmesine tıklayın / Give your voice command and click the "Stop" button
3. Yapay zeka tarafından oluşturulan görseli görüntüleyin ve indirin / View and download the AI-generated visual
4. İsteğe bağlı olarak, "Son Resmi Kullan" seçeneğini işaretleyerek önceki görseli referans alarak yeni bir görsel oluşturun / Optionally, generate a new visual based on the previous one by checking the "Use Latest Image" option

## Lisans / License

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

This project is licensed under the MIT License. See the `LICENSE` file for more information.