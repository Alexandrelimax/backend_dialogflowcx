from typing import Protocol

class ISpeechToText(Protocol):
    def transcribe(self, audio_bytes: bytes) -> str:
        ...
