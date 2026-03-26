import logging
import os
from datetime import datetime

LOG_FILE = None

def get_logger(name):

    global LOG_FILE

    if LOG_FILE is None:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        log_dir = os.path.join(BASE_DIR, "logs")
        os.makedirs(log_dir, exist_ok=True)

        LOG_FILE = os.path.join(
            log_dir,
            f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 🔥 Prevent duplicate handlers
    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.propagate = False

    return logger