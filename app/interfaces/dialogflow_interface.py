from typing import Dict, Protocol

class IDialogflow(Protocol):
    async def detect_intent(self, text: str) -> Dict[str, any]:
        """Detects the intent of the provided text using Dialogflow CX."""
        ...