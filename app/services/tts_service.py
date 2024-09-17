from app.interfaces.tts_interface import ITextToSpeech
from google.cloud.texttospeech import *

class TextToSpeechService(ITextToSpeech):
    def __init__(self, project_id: str):
        self.client = TextToSpeechClient()
        self.project_id = project_id

    def synthesize_speech(self, text: str) -> bytes:

        synthesis_input = SynthesisInput(text=text)
        
        voice = VoiceSelectionParams(
            language_code="pt-BR", 
            name="pt-BR-Wavenet-D", 
            ssml_gender=SsmlVoiceGender.NEUTRAL
        )

        audio_config = AudioConfig(audio_encoding=AudioEncoding.LINEAR16)

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response.audio_content
