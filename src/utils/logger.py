import logging
from pathlib import Path

from src.utils.paths import LOG_DIR

LOG_FILE = LOG_DIR / "app.log"

def get_logger(name: str) -> logging.Logger: # Type hint
    logger = logging.getLogger(name) # Gets an existing logger or creates one if it doesn't exist
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger # Prevents duplicate handlers on the same logger
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger