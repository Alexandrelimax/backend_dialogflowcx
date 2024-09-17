from fastapi import Depends

from app.interfaces.chatbot_interface import IChatBot
from app.interfaces.stt_interface import ISpeechToText
from app.interfaces.dialogflow_interface import IDialogflow
from app.interfaces.tts_interface import ITextToSpeech

from app.services.chatbot_service import ChatBotService
from app.services.stt_service import SpeechToTextService
from app.services.dialogflow_service import DialogflowService
from app.services.tts_service import TextToSpeechService

def get_speech_to_text_service() -> ISpeechToText:
    return SpeechToTextService(project_id="your-project-id", location="us-central1")

def get_dialogflow_service() -> IDialogflow:
    return DialogflowService(project_id="your-project-id")

def get_text_to_speech_service() -> ITextToSpeech:
    return TextToSpeechService(project_id="your-project-id")

def get_chat_bot_service(
    speech_to_text_service: ISpeechToText = Depends(get_speech_to_text_service),
    dialogflow_service: IDialogflow = Depends(get_dialogflow_service),
    text_to_speech_service: ITextToSpeech = Depends(get_text_to_speech_service)
) -> IChatBot:
    return ChatBotService(speech_to_text_service, dialogflow_service, text_to_speech_service)


