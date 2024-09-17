from core.context.conversation_buffer_memory import BufferMemory
from .handler_config import configure_handlers
from app.interfaces.intent_handler_interface import IntentHandlerInterface
from typing import  Dict

class IntentHandler:
    
    def __init__(self):
        self.memory = BufferMemory()
        self.factory = configure_handlers()

    def handle(self, intent_name: str, fulfillment_text: str) -> Dict[str, str]:
        handler_class = self.factory.get_handler(intent_name)
        
        if handler_class:
            handler = handler_class(self.memory)
            return handler.handle(fulfillment_text)
        return {"message": "Intenção não reconhecida."}
