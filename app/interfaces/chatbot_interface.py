from typing import Protocol

class IChatBot(Protocol):
    async def process_audio(self, audio: bytes, session_id: str) -> dict:
        ...

    async def process_text(self, text: str, session_id: str) -> dict:
        ...
