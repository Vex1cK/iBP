import logging
logger = logging.getLogger(__name__)

import json

from src.config.config import config_file_path, update_USER_TOKEN

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