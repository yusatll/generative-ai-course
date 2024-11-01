from openai import OpenAI  
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("openai_api_key")

client = OpenAI(
    api_key=my_key
)

# Whisper API ile ses dökümanı oluşturma fonksiyonu
# Function to transcribe audio using Whisper API
def transcribe_with_whisper(audio_filename):
    audio_file = open(audio_filename, "rb")

    ai_gen_transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="tr"
    )

    return ai_gen_transcript.text