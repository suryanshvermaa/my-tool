from listenSpeak import listen,speak
from functions import execute_command

speak("Hello! I am Jarvis. How can I assist you?")
while True:
    command = listen()
    if command:
        execute_command(command)
