from listenSpeak import listen,speak
from system_instruct import system_instruction
from tools import tools
from gemini import genAi
import json

def execute_function(function_name, function_input):
    """Execute predefined functions based on Gemini's output"""
    if function_name == "get_time":
        return tools.open_terminal()
    elif function_name == "open_app":
        app_name = function_input if function_input else "Unknown app"
        return tools.open_app(app_name)
    elif function_name == "shut_down":
        return tools.shut_down()
    elif function_name == "bye":
        return tools.bye()
    elif function_name == "open_folder":
        folder_name=function_input if function_input else "Unknown folder"
        return tools.open_folder(folder_name)
    elif function_name == "open_folder_in_vs_code":
        folder_name=function_input if function_input else "Unkown folder"
    elif function_name == "run_mailer":
        return tools.run_mailer()
    elif function_name == "open_docker":
        return tools.open_docker()
    elif function_name == "open_website":
        url=function_input if function_input else "Unknown url"
        return tools.open_website(url)
    elif function_name == "search_youtube":
        content=function_input if function_input else "Unknown content"
        return tools.search_youtube(content)
    elif function_name == "open_terminal":
        return tools.open_terminal()
    else:
        return f"Function {function_name} not recognized."
    

def ask_gemini(user_query):
    """Send a query to Gemini AI with system prompt"""
    # 🔹 Define the conversation with the system prompt
    # userMessage={"type":"user","user":user_query}
    # conversation.append({"role":"user","content":json.dumps(userMessage)})
    # response = model.generate_content(conversation)
    # response_json = json.loads(response.text)
    if "type" in response_json and response_json["type"] == "action":
        function_name = response_json["function"]
        function_input = response_json.get("input", None)
        functionResponse=execute_function(function_name, function_input)

        
# response = ask_gemini()
# print(response)
conversation = [
    {"role":"system","content":system_instruction()}
]
speak("Hello! I am Jarvis. How can I assist you?")
while True:
    userQuery = listen()
    if userQuery:
        userMessage={"type":"user","user":userQuery}
        conversation.append({"role":"user","content":json.dumps(userMessage)})
        while True:
            model=genAi()
            response = model.generate_content(conversation)
            conversation.append({"role":"assistant","content":response.text})
            response_json = json.loads(response.text)
            if "type" in response_json and response_json["type"] == "output":
                speak(response_json.output)
                print(response_json.output)
                break
            elif "type" in response_json and response_json["type"] == "action":
                fn=response_json.function
                params=response_json.input
                obervation=execute_function(fn, params)
                obervationMessage={
                    "type":"observation",
                    "observation":"observation"
                }
                conversation.append(obervationMessage)




        