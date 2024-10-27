import ctypes
from ctypes import HRESULT
import logging

logging.basicConfig(level=logging.INFO)


# Определение констант
COINIT_APARTMENTTHREADED = 0x2  # STA модель
COINIT_MULTITHREADED = 0x0      # MTA модель
S_OK = 0
S_FALSE = 1

# Попытка инициализации COM
result = ctypes.windll.ole32.CoInitializeEx(None, COINIT_APARTMENTTHREADED)

if result == 0:
    logging.info("COM initialized")
elif result == 1:
    logging.info("COM has already been initialized in this thread")
else:
    logging.error(f"COM initialization error: {result}")
