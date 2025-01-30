import json
import os

loggers_level = 10
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0
# FATAL = CRITICAL
# WARN = WARNING

here = os.getcwd()
here_src = os.path.join(here, 'src')
config_file_path = os.path.join(here_src, 'config', 'config.json')

with open(config_file_path, 'r') as file:
    config = json.load(file)

NONE_VALUE = config['none_value']
PATH_TO_APP_ICON = os.path.join(here, "src", "config", config['app_icon_name'])
SERVER_URL = config['server_url']

AUDIO_PATH = os.path.join(here, config['audio_path']) if not os.path.isabs(config['audio_path']) \
    else config['audio_path']
FULL_TEXT_PATH = os.path.join(here, config['full_text_path']) if not os.path.isabs(config['full_text_path']) \
    else config['full_text_path']
SUM_TEXT_PATH = os.path.join(here, config['sum_text_path']) if not os.path.isabs(config['sum_text_path']) \
    else config['sum_text_path']
FOLDER_PATH = os.path.join(here, config['folder_path']) if not os.path.isabs(config['folder_path']) \
    else config['folder_path']

USER_TOKEN = config['token']
HAVE_TOKEN = USER_TOKEN != NONE_VALUE

def update_USER_TOKEN():
    global HAVE_TOKEN, USER_TOKEN
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    USER_TOKEN = config['token']
    HAVE_TOKEN = USER_TOKEN != NONE_VALUE

def update_SERVER_URL():
    global SERVER_URL
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    SERVER_URL = config['server_url']

def get_current_status():
    global HAVE_TOKEN
    return HAVE_TOKEN

def get_current_token():
    global USER_TOKEN
    return USER_TOKEN