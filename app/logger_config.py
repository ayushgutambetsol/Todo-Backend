import logging
import os
import sys


def custom_logger(logger):
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout) if "DYNO" in os.environ else \
        logging.FileHandler('app_service.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
