class ChatBotException(Exception):
    """Base class for all chatbot exceptions."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class TranscriptionError(Exception):
    """Exception raised for errors in speech-to-text transcription."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class DialogflowError(Exception):
    """Exception raised for errors in Dialogflow."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class SynthesisError(Exception):
    """Exception raised for errors in text-to-speech synthesis."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class DialogflowError(Exception):
    """Exception raised for errors in Dialogflow."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message