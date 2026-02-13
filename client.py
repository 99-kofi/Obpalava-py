from gradio_client import Client
from .exceptions import ObalaPalavaError

DEFAULT_SPACE = "Willie999/obalapalava-demo"

class ObalaPalavaClient:
    def __init__(self, space=DEFAULT_SPACE):
        try:
            self.client = Client(space)
        except Exception as e:
            raise ObalaPalavaError(f"Failed to connect to ObalaPalava API: {e}")

    def translate(self, text: str):
        if not text or not isinstance(text, str):
            raise ObalaPalavaError("Input text must be a non-empty string")

        try:
            result = self.client.predict(
                text=text,
                api_name="/translate_pidgin"
            )
            return result
        except Exception as e:
            raise ObalaPalavaError(f"Translation failed: {e}")
