from typing import Protocol

class ITextToSpeech(Protocol):
    def synthesize_speech(self, text: str) -> bytes:
        ...
