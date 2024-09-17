from langchain.memory import ConversationBufferMemory

class BufferMemory:
    def __init__(self):
        self.memory = ConversationBufferMemory()

    def add_message(self, role: str, message: str):
        self.memory.add_message(role, message)

    def get_history(self) -> str:
        return self.memory.get_history()

    def clear_memory(self):
        self.memory.clear()
