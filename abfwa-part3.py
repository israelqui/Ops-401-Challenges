#!/usr/bin/env python3
# Script Name: Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Description: This script uses Python brute force tool that includes a new mode for attacking password-locked zip files:
# Author: Israel Quirola
# Date: February, 2024

import zipfile
import time

def zip_brute_force(zip_file_path, word_list_path):
    with open(word_list_path, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                # Open the password-protected zip file
                with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                    # Try to extract a file from the zip using the current password
                    zip_file.extract('dummy_file', pwd=password.encode('utf-8'))

                # If extraction is successful, print the password and break the loop
                print(f"Successful extraction - Password: {password}")
                break

            except zipfile.BadZipFile:
                # If the zip file is invalid, print an error message and exit
                print("Error: Invalid zip file.")
                break

            except RuntimeError:
                # If the password is incorrect, continue to the next password
                print(f"Failed extraction attempt - Password: {password}")
                time.sleep(1)  # Add a delay of 1 second between attempts

            except Exception as e:
                # Handle other exceptions (e.g., file not found, etc.)
                print(f"Error: {e}")

def main():
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. SSH Brute Force")
    print("3. Zip File Brute Force")

    mode = input("Enter the mode number (1, 2, or 3): ")

    if mode == "1":
        word_list_path = input("Enter the path to the word list file: ")
        offensive_mode(word_list_path)

    elif mode == "2":
        ip_address = input("Enter the IP address of the SSH server: ")
        username = input("Enter the SSH username: ")
        word_list_path = input("Enter the path to the word list file: ")
        ssh_brute_force(ip_address, username, word_list_path)

    elif mode == "3":
        zip_file_path = input("Enter the path to the password-locked zip file: ")
        word_list_path = input("Enter the path to the word list file: ")
        zip_brute_force(zip_file_path, word_list_path)

    else:
        print("Invalid mode selection. Please enter either '1', '2', or '3'.")

if __name__ == "__main__":
    main()