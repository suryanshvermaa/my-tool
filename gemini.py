from api import get_api_key
import google.generativeai as genai

genai.configure(api_key=get_api_key())
def genAi():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
    )
    return model

