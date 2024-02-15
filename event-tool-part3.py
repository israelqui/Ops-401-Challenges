#!/usr/bin/env python3
# Script Name: Event Logging Tool Part 3 of 3
# Description: Python script that demonstrates log rotation capabilities:
# Author: Israel Quirola
# Date: February 15, 2024

# Import libraries
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
import sys

# Create our logger object
logger = logging.getLogger('my_logger')

# logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler('logs.log'), ])

# Create handlers

# File handler, set level of message to warning
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.WARNING)

# Stream handler, set level of message to capture error
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.ERROR)

# Create formatters for the headers 
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
s_format = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')

# Tell the formatters 
f_handler.setFormatter(f_format)
s_handler.setFormatter(s_format)

# Tell the handlers to work with specific logger
logger.addHandler(f_handler)
logger.addHandler(s_handler)

logger.warning("This is a warning!")
logger.error("This is an error")

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