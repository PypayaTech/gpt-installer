import platform
from typing import List, Dict, Any
import openai


def check_operating_system():
    return platform.system()


def load_text_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def get_openai_api_reply(input_messages: List[Dict[str, Any]], model: str = "gpt-4", temperature: float = 0.1) -> str:
    """
    Generates a reply from the given input.

    Args:
        input_messages (List[Dict[str, Any]]): A list of message dictionaries to be processed by the model.
        model (str): Identifier for the language model to be used.
        temperature (float): Controls randomness in the generation. Lower is less random.

    Returns:
        str: The content of the response from the assistant.
    """
    response = openai.ChatCompletion.create(messages=input_messages, model=model, temperature=temperature)
    response_content = response.choices[0].message["content"]
    return response_content
