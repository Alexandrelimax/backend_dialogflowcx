import uuid
def generate_session_id() -> str:
    """Gera um session_id único."""
    return str(uuid.uuid4())