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
AUDIO_PATH = os.path.join(here, config['audio_path'])
SERVER_URL = config['server_url']

USER_TOKEN = config['token']
HAVE_TOKEN = USER_TOKEN != NONE_VALUE

def update_USER_TOKEN():
    global HAVE_TOKEN, USER_TOKEN
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    USER_TOKEN = config['token']
    HAVE_TOKEN = USER_TOKEN != NONE_VALUE

def get_current_status():
    global HAVE_TOKEN
    return HAVE_TOKEN

def get_current_token():
    global USER_TOKEN
    return USER_TOKEN