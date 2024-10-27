import json
import os

with open(os.path.join(os.getcwd(), 'config.json')) as file:
    config = json.load(file)

AUDIO_PATH = os.path.join(os.getcwd(), config['audio_path'])