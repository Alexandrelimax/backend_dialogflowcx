from app.interfaces.dialogflow_interface import IDialogflow
from app.errors import DialogflowError

from google.cloud import dialogflowcx_v3beta1 as dialogflow
from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import MessageToDict


class DialogflowCXService(IDialogflow):
    def __init__(self, project_id: str, agent_id: str, location: str):
        self.client = dialogflow.SessionsClient()
        self.project_id = project_id
        self.agent_id = agent_id
        self.location = location


    def detect_intent(self, text: str, session_id: str = "your-session-id", language_code: str = "en-US") -> str:

        session_path = self._session_path(session_id)

        text_input = dialogflow.TextInput(text=text)
        
        query_input = dialogflow.QueryInput(text=text_input, language_code=language_code)
        
        # Realizando a chamada para o Dialogflow CX
        request = dialogflow.DetectIntentRequest(session=session_path, query_input=query_input)
        
        try:
            response = self.client.detect_intent(request=request)

            response_dict = MessageToDict(response._pb)
            return response_dict['queryResult']['responseMessages'][0]['text']['text'][0]
        except Exception as e:
            raise DialogflowError(f"Error during Dialogflow CX call: {str(e)}")



    def _session_path(self, session_id: str) -> str:
        return f"projects/{self.project_id}/locations/{self.location}/agents/{self.agent_id}/sessions/{session_id}"    

