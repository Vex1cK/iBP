from dotenv import load_dotenv
import platform
import os

load_dotenv()

loggers_level = 10
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0
# FATAL = CRITICAL
# WARN = WARNING

DB_NAME = os.getenv("DB_NAME")
ICO_NAME = os.getenv("ICO_NAME")
STATIC_DIR_NAME = os.getenv("STATIC_DIR_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_HOSTNAME = os.getenv("SMTP_HOSTNAME")

FRONTEND_URL = os.getenv("FRONTEND_URL")

SMTP_PORT = int(os.getenv("SMTP_PORT"))

DB_NAME_TEST = os.getenv("DB_NAME_TEST")

here = os.getcwd()

path_1 = 'backend\\src'
path_2 = 'app\\src'

path_1_05 = 'backend'
path_2_05 = 'app'

if platform.system() != "Windows":
    path_1 = path_1.replace("\\", '/')
    path_2 = path_2.replace("\\", '/')

if not (here.endswith(os.path.normpath(path_1)) or here.endswith(os.path.normpath(path_2))):
    if here.endswith(path_1_05) or here.endswith(path_2_05):
        here = os.path.join(here, 'src')
    else:
        raise Exception("Какая-то проблема с путями, очень издалека всё запускается видимо")

PATH_TO_USERS_AUDIO_FILES = os.path.join(here, os.path.join("ML_api", "users_audios"))
PATH_TO_USERS_TXT_FILES = os.path.join(here, os.path.join("ML_api", "users_texts"))
PATH_TO_OUTPUTS_FILES = os.path.join(here, os.path.join("ML_api", "output_files"))

paths_need_to_check = [
    PATH_TO_USERS_TXT_FILES,
    PATH_TO_USERS_AUDIO_FILES,
    PATH_TO_OUTPUTS_FILES
]

PATH_TO_A2T_MODEL = os.path.join(here, "..", 'ai_models', 'audio2text', "whisper-large-v3")
PATH_TO_SUM_MODEL = os.path.join(here, "..", 'ai_models', 'text2text_summary', "bert-large-uncased")

paths_to_models_to_check = [
    PATH_TO_A2T_MODEL,
    PATH_TO_SUM_MODEL
]

ICO_PATH = os.path.join(here, os.path.join(STATIC_DIR_NAME, ICO_NAME))

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30