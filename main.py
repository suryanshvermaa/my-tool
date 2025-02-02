from listenSpeak import listen,speak
from tools import tools
from gemini import genAi
import json

def execute_function(function_name, function_input):
    """Execute predefined functions based on Gemini's output"""
    if function_name == "get_time":
        open_terminal=tools["open_terminal"]
        return open_terminal()
    elif function_name == "open_app":
        app_name = function_input if function_input else "Unknown app"
        open_app=tools["open_app"]
        return open_app(app_name)
    elif function_name == "shut_down":
        shut_down=tools["shut_down"]
        return shut_down()
    elif function_name == "bye":
        bye=tools["bye"]
        return bye()
    elif function_name == "open_folder":
        folder_name=function_input if function_input else "Unknown folder"
        open_folder=tools["open_folder"]
        return open_folder(folder_name)
    elif function_name == "open_folder_in_vs_code":
        folder_name=function_input if function_input else "Unkown folder"
        open_folder_in_vs_code=tools["open_folder_in_vs_code"]
        return open_folder_in_vs_code(folder_name)
    elif function_name == "run_mailer":
        run_mailer=tools["run_mailer"]
        return run_mailer()
    elif function_name == "open_docker":
        open_docker=tools["open_docker"]
        return open_docker()
    elif function_name == "open_website":
        url=function_input if function_input else "Unknown url"
        open_website=tools["open_website"]
        return open_website(url)
    elif function_name == "search_youtube":
        content=function_input if function_input else "Unknown content"
        search_youtube=tools["search_youtube"]
        return search_youtube(content)
    elif function_name == "open_terminal":
        open_terminal=tools["open_terminal"]
        return open_terminal()
    else:
        return f"Function {function_name} not recognized."
     
def aiChat(userQuery,chat):
    userMessage={"type":"user","user":userQuery}
    response=chat.send_message(json.dumps(userMessage))
    response_content = response._result.candidates[0].content.parts[0].text
    print(response_content)
    response_json = json.loads(response_content.strip("```json\n").strip("```"))
    if "type" in response_json and response_json["type"] == "output":
        speak(response_json["output"])
        print(response_json["output"])
        return
    elif "type" in response_json and response_json["type"] == "action":
        fn=response_json["function"]
        params=response_json["input"]
        obervation=execute_function(fn, params)
        obervationMessage={
            "type":"observation",
            "observation":obervation
        }
        print(obervationMessage)
        aiChat(json.dumps(obervationMessage),chat)

conversation = [
    {"role":"user","parts":"Hi!"}
]
speak("Hello! I am Jarvis. How can I assist you?")
while True:
    userQuery = listen()
    if userQuery:
        model=genAi()
        chat = model.start_chat(history=conversation)
        aiChat(userQuery,chat)

        




        