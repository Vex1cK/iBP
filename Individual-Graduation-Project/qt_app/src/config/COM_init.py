import logging
logger = logging.getLogger(__name__)

import ctypes
from ctypes import HRESULT  # noqa: F401 # type: ignore

# Определение констант
COINIT_APARTMENTTHREADED = 0x2  # STA модель
COINIT_MULTITHREADED = 0x0      # MTA модель
S_OK = 0
S_FALSE = 1

# Попытка инициализации COM
result = ctypes.windll.ole32.CoInitializeEx(None, COINIT_APARTMENTTHREADED)

if result == S_OK:
    logger.debug("COM initialized")
elif result == S_FALSE:
    logger.debug("COM has already been initialized in this thread")
else:
    logger.error(f"COM initialization error: {result}")
