from api import get_api_key
from system_instruct import system_instruction
import google.generativeai as genai

genai.configure(api_key=get_api_key())
def genAi():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction()
    )
    return model

