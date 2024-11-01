# Audio Processing Project

This project is a Streamlit-based web application that demonstrates various audio processing capabilities using AI models. It includes functionality for text-to-speech synthesis, speech-to-text transcription, and audio translation.

## Features

1. **Text-to-Speech (TTS)**: Generate speech from text using OpenAI's TTS model with various voice options.
2. **Whisper Transcription**: Transcribe audio files to text using OpenAI's Whisper model.
3. **Whisper Translation**: Translate audio files to English text using OpenAI's Whisper model.
4. **Conformer Transcription**: Transcribe audio files to text using AssemblyAI's Conformer model.

## Prerequisites

Before running this project, you need to have the following:

- Python 3.6 or higher
- OpenAI API key
- AssemblyAI API key

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
   assemblyai_apikey=your_assemblyai_api_key_here
   ```

## Usage

Run the Streamlit app:
```
streamlit run ses.py
```

The application will open in your default web browser with four tabs:

1. **TTS ses sentezleme (TTS Speech Synthesis)**: Enter text and choose a voice to generate speech.
2. **Whisper transkripsion (Whisper Transcription)**: Upload a WAV file to transcribe it to text.
3. **Whisper Tercüme (Whisper Translation)**: Upload an MP3 file to translate it to English text.
4. **Conformer Transkripsion (Conformer Transcription)**: Upload a WAV file to transcribe it to text using the Conformer model.

## Note

- Ensure you have sufficient API credits and comply with the usage policies of OpenAI and AssemblyAI when using this application.
- The application currently supports WAV files for Whisper and Conformer transcription, and MP3 files for Whisper translation. Make sure your audio files are in the correct format.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/project/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)