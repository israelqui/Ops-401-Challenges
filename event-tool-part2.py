#!/usr/bin/env python3
# Script Name: Event Logging Tool Part 2 of 3
# Description: Python script that demonstrates log rotation capabilities:
# Author: Israel Quirola
# Date: February 14, 2024

# Import libraries
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with log rotation
# create a log formatter using the Formatter class from the logging module. This formatter specifies the format of each log message. In this case, it includes the timestamp (%(asctime)s), log level (%(levelname)s), and the actual log message (%(message)s).
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# We set the formatter for the log handler using the setFormatter() method. This ensures that each log message written to the file follows the specified format.
log_handler = RotatingFileHandler(filename='example.log', mode='a', maxBytes=1024*1024, backupCount=5, encoding=None, delay=0)
log_handler.setFormatter(log_formatter)

# retrieve the root logger using getLogger() method. add the log handler (log_handler) to the root logger. This means that any log messages emitted by the logger or its children will be processed by this handler. set the logging level of the root logger to DEBUG. This means that all log messages with a severity level of DEBUG or higher will be processed by the logger and its handlers.
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

# script remains the same from last time
def divide_numbers(x, y):
    try:
        result = x / y
        logging.info(f'Division result: {result}')
        return result
    except ZeroDivisionError as e:
        logging.error(f'Error occurred: {e}')
        return None

def main():
    # Perform some calculations
    logging.info('Starting the program...')
    result1 = divide_numbers(10, 2)
    result2 = divide_numbers(8, 0)  # Intentionally induce an error
    result3 = divide_numbers(20, 4)
    logging.info('Program finished.')

if __name__ == "__main__":
    main()