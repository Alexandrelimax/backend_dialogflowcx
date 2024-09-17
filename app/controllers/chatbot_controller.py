from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional
from app.interfaces.chatbot_interface import IChatBot

class ChatBotController:
    def __init__(self, chat_bot_service: IChatBot):
        self.chat_bot_service = chat_bot_service
        self.router = APIRouter()
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/audio", self.chat_with_audio, methods=["POST"])
        self.router.add_api_route("/text", self.chat_with_text, methods=["POST"])


    async def chat_with_audio(self, audio_data: bytes, session_id: Optional[str] = None):
        try:
            response = await self.chat_bot_service.process_audio(audio_data, session_id)
            return JSONResponse(content={"response": response, "session_id": session_id})
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


    async def chat_with_text(self, text: str, session_id: Optional[str] = None):

        try:
            response = await self.chat_bot_service.process_text(text, session_id)
            return JSONResponse(content={"response": response, "session_id": session_id})
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
