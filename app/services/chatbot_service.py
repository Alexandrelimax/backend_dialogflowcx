from fastapi import HTTPException

from app.interfaces.chatbot_interface import IChatBot
from app.interfaces.stt_interface import ISpeechToText
from app.interfaces.dialogflow_interface import IDialogflow
from app.interfaces.tts_interface import ITextToSpeech

from app.errors import TranscriptionError, DialogflowError, SynthesisError

class ChatBotService(IChatBot):
    def __init__(
        self,
        speech_to_text_service: ISpeechToText,
        dialogflow_service: IDialogflow,
        text_to_speech_service: ITextToSpeech
    ):
        self.speech_to_text_service = speech_to_text_service
        self.dialogflow_service = dialogflow_service
        self.text_to_speech_service = text_to_speech_service


    async def process_audio(self, audio: bytes, session_id: str) -> dict:
        try:
            text = self.speech_to_text_service.transcribe(audio)
        except Exception as e:
            raise TranscriptionError(f"Error during transcription: {e}")

        try:
            response_text = await self.dialogflow_service.detect_intent(text, session_id)
        except Exception as e:
            raise DialogflowError(f"Error during Dialogflow processing: {e}")

        try:
            audio_content = await self.text_to_speech_service.synthesize_speech(response_text)
            return {"audio_content": audio_content}
        except Exception as e:
            raise SynthesisError(f"Error during synthesis: {e}")



    async def process_text(self, text: str, session_id: str) -> dict:
        try:
            response_text = await self.dialogflow_service.detect_intent(text, session_id)
            return {"text_content": response_text}
        except Exception as e:
            raise DialogflowError(f"Error during Dialogflow processing: {e}")

        

        