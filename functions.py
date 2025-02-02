import datetime
import webbrowser
import time
import os
import platform
from listenSpeak import listen,speak

def open_terminal():
    """Open the terminal based on the OS."""
    os_name = platform.system()
    if os_name == "Windows":
        os.system("start cmd")  # Open Command Prompt
    elif os_name == "Darwin":  # macOS
        os.system("open -a Terminal")
    elif os_name == "Linux":
        os.system("gnome-terminal")  # Works for Ubuntu/Gnome
    else:
        speak("I am not sure how to open a terminal on this system.")
        return
    
    speak("Opening terminal.")
    time.sleep(2)  # Wait for terminal to open

def get_time():
    now = datetime.datetime.now().strftime("%H:%M")
    return now

def bye():
    speak("Goodbye! Have a great day.")
    exit()

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)

def open_website(url):
    webbrowser.open(url)