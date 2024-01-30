#!/usr/bin/env python3
# Script Name: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Description: This script defines two functions (offensive_mode and defensive_mode) for the respective modes and a main function to handle user input and mode selection
# Author: Israel Quirola
# Date: January 30, 2024

import time

def offensive_mode(word_list_path):
    with open(word_list_path, 'r') as file:
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(1)  # Add a delay of 1 second between words

def defensive_mode(user_input, word_list_path):
    with open(word_list_path, 'r') as file:
        word_list = [line.strip() for line in file]
        if user_input in word_list:
            print(f"The input '{user_input}' is recognized as a valid password.")
        else:
            print(f"The input '{user_input}' is not found in the word list.")

def main():
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")

    mode = input("Enter the mode number (1 or 2): ")

    if mode == "1":
        word_list_path = input("Enter the path to the word list file: ")
        offensive_mode(word_list_path)
    elif mode == "2":
        user_input = input("Enter a string to search in the word list: ")
        word_list_path = input("Enter the path to the word list file: ")
        defensive_mode(user_input, word_list_path)
    else:
        print("Invalid mode selection. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
