#!/usr/bin/env python3
# Script Name: Event Logging Tool Part 1 of 3
# Description: Python script that demonstrates logging capabilities:
# Author: Israel Quirola
# Date: February 13, 2024

# Import libraries
import logging

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
    