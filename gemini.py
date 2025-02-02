from api import get_api_key
import google.generativeai as genai
from system_instruct import system_instruction

genai.configure(api_key=get_api_key())
def geniAi():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction
        )
    response = model.generate_content("Explain how AI works")
    print(response.text)
