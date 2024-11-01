# AI Image Generation Project

This project is a Streamlit-based web application that demonstrates the use of various AI models for image generation and manipulation. It includes functionality for generating images using DALL-E 3 and Stable Diffusion, as well as creating variations of existing images using DALL-E 3.

## Features

1. **DALL-E 3 Image Generation**: Generate images based on text prompts using OpenAI's DALL-E 3 model.
2. **DALL-E 3 Image Variation**: Create variations of uploaded PNG images using DALL-E 3.
3. **Stable Diffusion Image Generation**: Generate images using the Stable Diffusion model via the Stability AI API.

## Prerequisites

Before running this project, you need to have the following:

- Python 3.6 or higher
- OpenAI API key
- Stability AI API key

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys:
   ```
   chatgpt_apikey=your_openai_api_key_here
   stabilityai_apikey=your_stability_ai_api_key_here
   ```

## Usage

Run the Streamlit app:
```
streamlit run image.py
```

The application will open in your default web browser with three tabs:

1. **Resim Üret (Generate Image)**: Enter a text prompt to generate an image using DALL-E 3.
2. **Varyasyon Oluştur (Create Variation)**: Upload a PNG image and create variations using DALL-E 3.
3. **Stable Diffusion**: Enter a text prompt to generate an image using Stable Diffusion.

## Note

- The Stable Diffusion implementation currently saves the generated image as "lighthouse.webp" in the project directory. You may want to modify this behavior to display the image directly in the Streamlit interface or allow custom save locations.
- Ensure you have sufficient API credits and comply with the usage policies of OpenAI and Stability AI when using this application.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/project/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)