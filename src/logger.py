import logging

logging.basicConfig(
    filename='app.log',  # Specifies the log file
    level=logging.DEBUG,  # Sets the logging level
    encoding='utf-8',
    format='%(asctime)s [%(levelname)s] - %(message)s'  # Specifies the log format
)

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_critical(message):
    logging.critical(message)







