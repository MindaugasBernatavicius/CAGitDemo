import logging.config
import sys

import yaml

with open('..\config\main_config.yml', 'r') as config:
    logging.config.dictConfig(yaml.safe_load(config)['logging'])

main_logger = logging.getLogger('main')
error_logger = logging.getLogger('error')

class Calculator:
    def __init__(self):
        main_logger.info('Calculator instance created')

    def add(self, i, j):
        return i + j

    def multiply(self, i, j):
        return i * j

    def divide(self, i, j):
        try:
            return i / j
        except ZeroDivisionError as e:
            # error_logger.error('Division by 0')
            error_logger.exception('Division by 0')