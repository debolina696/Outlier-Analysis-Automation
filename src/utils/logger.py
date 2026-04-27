# =========================================
# Logger Module
# =========================================

import logging
import os


def setup_logger(log_folder):

    """
    Setup logger for pipeline execution
    """

    # Create logs folder if not exists
    if not os.path.exists(log_folder):

        os.makedirs(log_folder)

    log_file = os.path.join(
        log_folder,
        "pipeline.log"
    )

    # Create logger
    logger = logging.getLogger("pipeline_logger")

    logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(log_file)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:

        logger.addHandler(file_handler)

    logger.info("Logger initialized")

    print("📝 Logger setup complete")

    return logger
