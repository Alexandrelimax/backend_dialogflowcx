
from fastapi import FastAPI

from app.controllers.chatbot_controller import ChatBotController
from app.services.chatbot_service import ChatBotService
from app.services.stt_service import SpeechToTextService
from app.services.dialogflow_service import DialogflowCXService
from app.services.tts_service import TextToSpeechService

app = FastAPI()


speech_to_text_service = SpeechToTextService()
dialogflow_service = DialogflowCXService(project_id="your-project-id")
text_to_speech_service = TextToSpeechService()

chat_bot_service = ChatBotService(
    speech_to_text_service=speech_to_text_service,
    dialogflow_service=dialogflow_service,
    text_to_speech_service=text_to_speech_service
)


chat_bot_controller = ChatBotController(chat_bot_service)

app.include_router(chat_bot_controller.router)

@app.get("/")
def read_root():
    return {"message": "Teste API"}