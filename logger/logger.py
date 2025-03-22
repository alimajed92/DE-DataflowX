import logging
import colorlog
import os
from datetime import datetime


def setup_logger():
    log_dir = "logs"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("dataFlow_logger")

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)

    # Console Handler with Colors
    c_handler = logging.StreamHandler()
    log_filename = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d") + ".log")
    f_handler = logging.FileHandler(log_filename)

    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)

    # Colored formatter
    log_format = (
        "%(asctime)s - %(name)s - %(log_color)s%(levelname)s - %(message)s%(reset)s"
    )
    c_formatter = colorlog.ColoredFormatter(
        log_format,
        log_colors={
            "DEBUG": "blue",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    # Standard formatter for file logs
    f_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    c_handler.setFormatter(c_formatter)
    f_handler.setFormatter(f_formatter)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


dataFlow_logger = setup_logger()
