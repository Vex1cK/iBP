import logging
logger = logging.getLogger(__name__)

import ipaddress
import json

from src.config.config import config_file_path, NONE_VALUE, USER_TOKEN, update_USER_TOKEN, update_SERVER_URL
from src.server.auth_ping_api_client import logout, update_token_in_auth_module

def is_valid_ipv4(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

def update_token_in_json_and_config(new_token):
    key = 'token'
    with open(config_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if key in data:
        data[key] = new_token
    else:
        raise KeyError(f"Key '{key}' not found in the JSON file.")
    
    with open(config_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    logger.debug(f"Token updated in JSON file: {new_token}")
    update_USER_TOKEN()
    return True

def update_all_paths(new_paths):
    keys = ['audio_path', 'full_text_path', 'sum_text_path', 'folder_path']

    if len(new_paths) != len(keys):
        return False
    
    with open(config_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for i in range(len(keys)):
        key = keys[i]
        new_path = new_paths[i]
        if key in data:
            data[key] = new_path
        else:
            raise KeyError(f"Key '{key}' not found in the JSON file.")
    
    with open(config_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    logger.debug("All paths updated in JSON file")
    return True

def logout_util():
    logout(USER_TOKEN)

    key = 'token'
    with open(config_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if key in data:
        data[key] = NONE_VALUE
    else:
        raise KeyError(f"Key '{key}' not found in the JSON file.")
    
    with open(config_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    logger.debug(f"Token updated in JSON file: {NONE_VALUE}")
    update_USER_TOKEN()
    return True

def change_server_IP(new_ip: str):
    key = 'server_url'
    with open(config_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if key in data:
        data[key] = "http://" + new_ip
    else:
        raise KeyError(f"Key '{key}' not found in the JSON file.")
    
    with open(config_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    logger.debug(f"Server url updated in JSON file: {new_ip}")
    update_SERVER_URL()
    update_token_in_auth_module()
    return True