import logging

FOCUS_LOGGER_NAME = "eFocus"
LOGGER = logging.getLogger(FOCUS_LOGGER_NAME)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)
