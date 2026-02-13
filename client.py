from gradio_client import Client
from .exceptions import ObalaPalavaError
from .utils import validate_text

DEFAULT_SPACE = "Willie999/obalapalava-demo"
DEFAULT_API = "/translate_pidgin"

class ObalaPalavaClient:
    """
    Python client for ObalaPalava hosted API
    """

    def __init__(self, space: str = DEFAULT_SPACE):
        try:
            self.client = Client(space)
        except Exception as e:
            raise ObalaPalavaError(
                f"Could not connect to ObalaPalava Space '{space}': {e}"
            )

    def translate(self, text: str):
        """
        Translate English ↔ Pidgin using hosted ObalaPalava API
        """
        try:
            text = validate_text(text)

            result = self.client.predict(
                text=text,
                api_name=DEFAULT_API
            )

            return result

        except Exception as e:
            raise ObalaPalavaError(f"Translation failed: {e}")
