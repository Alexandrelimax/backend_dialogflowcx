from app.interfaces.stt_interface import ISpeechToText
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import *


class SpeechToTextService(ISpeechToText):
    def __init__(self, project_id: str):
        self.client = SpeechClient()
        self.project_id = project_id

    def transcribe(self, audio_file: str) -> RecognizeResponse:
        
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()

        # Configurações de reconhecimento
        config = RecognitionConfig(
            auto_decoding_config=AutoDetectDecodingConfig(),
            language_codes=["pt-BR"],
            model="long",
        )

        # Cria o request com as configurações e o conteúdo do áudio
        request = RecognizeRequest(
            recognizer=f"projects/{self.project_id}/locations/global/recognizers/_",
            config=config,
            content=audio_bytes,
        )

        # Chama o cliente para reconhecer o áudio
        response = self.client.recognize(request=request)

        # Retorna a transcrição da primeira alternativa do primeiro resultado
        if response.results:
            return response.results[0].alternatives[0].transcript
        return None