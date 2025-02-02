from functions import open_terminal,search_youtube,get_time,bye,open_website
from open_app import open_docker,open_folder_in_vs_code,open_folder,shut_down,run_mail_js,open_app

tools={
    "open_terminal":open_terminal,
    "search_youtube":search_youtube,
    "get_time":get_time,
    "bye":bye,
    "open_website":open_website,
    "open_docker":open_docker,
    "open_folder_in_vs_code":open_folder_in_vs_code,
    "open_folder":open_folder,
    "shut_down":shut_down,
    "run_mailer":run_mail_js,
    "open_app":open_app
}

# - open_folder_in_vs_code(folder_name:string): takes parameter folder_name and opens that folder in vs-code
# - search_youtube(content:string): takes parameter content as string and search on youtube that content
# - get_time(): returns current time
# - bye(): exit the chat between you and user
# - open_website(url:string): takes url as a parameter and opens in browser
# - open_docker(): opens docker in pc
# - open_folder(): opens a particular folder takes base path as desktop
# - shut_down(): shut down the whole computer
# - open_app(app:string): takes app parameter as string and open a particular app
#     apps-> {notepad,calculator,chrome,vlc}
# - open_terminal: open terminal in pc
# - run_mailer(): opens mail tool on terminal