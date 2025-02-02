import os
import subprocess

def open_folder_in_vs_code(folder_name):

    base_path = "C:\\Users\\surya\\OneDrive\\Desktop"
    folder_path = os.path.join(base_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ Folder '{folder_name}' created successfully.")
    else:
        print(f"⚠ Folder '{folder_name}' already exists.")

    subprocess.run(["code", folder_path], shell=True)
    print(f"🚀 Opened '{folder_name}' in VS Code.")
    return "openned"

def open_docker():
    """Opens Docker Desktop"""
    docker_path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
    os.startfile(docker_path)
    return "openned"

def open_folder(path):
    """Opens a specific folder"""
    folder_path = "C:\\Users\\surya\\OneDrive\\Desktop\\"+path
    os.startfile(folder_path)
    return "openned"

def run_mail_js():
    """Runs Mail tools.js in terminal"""
    mail_script_path = "C:\\Users\\surya\\OneDrive\\Desktop\\Mail\\tool.js"
    command = f'cmd /k "node {mail_script_path}"'
    subprocess.Popen(command, shell=True)
    return "openned"

def open_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", 
    }
    if app_name in apps:
        os.startfile(apps[app_name])
    else:
        print("App not found!")
    return "openned"

def shut_down():
    os.system("shutdown /s /t 0")
