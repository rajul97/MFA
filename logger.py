# logger.py

import logging

logging.basicConfig(
    filename="mfa_audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message, level="info"):
    """
    Logs events to the audit log.
    """
    if level.lower() == "info":
        logging.info(message)
    elif level.lower() == "warning":
        logging.warning(message)
    elif level.lower() == "error":
        logging.error(message)
