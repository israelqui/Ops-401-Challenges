#!/usr/bin/env python3
# Script Name: Web Application Fingerprinting 
# Description: Python script that utilizes multiple banner grabbing approaches against a single target.
# Author: Israel Quirola
# Date: February 26, 2024

# script for kali linux
import subprocess

# This function netcat_banner_grabbing is defined to perform banner grabbing using Netcat. It tries to execute the Netcat command with the specified options (-v for verbose, -n for numeric-only IP addresses, -z for scanning without sending any data, -w 1 for setting a timeout of 1 second) against the target address and port. If file not found it suggests the user to install it.
def netcat_banner_grabbing(target, port):
    try:
        result = subprocess.run(['nc', '-v', '-n', '-z', '-w', '1', target, str(port)], capture_output=True, text=True)
        print("Netcat Banner Grabbing Results:")
        print(result.stdout)
    except FileNotFoundError:
        print("Netcat is not installed. Please install Netcat (nc) to perform banner grabbing using this method.")

# This function telnet_banner_grabbing is defined to perform banner grabbing using Telnet. It tries to execute the Telnet command with a timeout of 1 second (timeout 1) against the target address and port. The input b'/' is sent to the Telnet process, which is essentially a meaningless command (/), just to trigger a response from the server. The capture_output=True parameter captures the output of the command, and text=True converts the output to text.
def telnet_banner_grabbing(target, port):
    try:
        result = subprocess.run(['timeout', '1', 'telnet', target, str(port)], input=b'/', capture_output=True, text=True)
        print("\nTelnet Banner Grabbing Results:")
        print(result.stdout)
    except FileNotFoundError:
        print("Telnet is not installed. Please install Telnet to perform banner grabbing using this method.")

# This function nmap_banner_grabbing is defined to perform banner grabbing using Nmap. It tries to execute the Nmap command with the options -sV for version detection and -p- to scan all 65535 TCP ports against the target address. 
def nmap_banner_grabbing(target):
    try:
        print("\nNmap Banner Grabbing Results:")
        subprocess.run(['nmap', '-sV', '-p-', target])
    except FileNotFoundError:
        print("Nmap is not installed. Please install Nmap to perform banner grabbing using this method.")

# This main function is defined to prompt the user to enter the target URL or IP address and the port number. Then it calls the three banner grabbing functions (netcat_banner_grabbing, telnet_banner_grabbing, nmap_banner_grabbing) with the specified target and port
def main():
    target = input("Enter the target URL or IP address: ")
    port = int(input("Enter the port number: "))
    
    netcat_banner_grabbing(target, port)
    telnet_banner_grabbing(target, port)
    nmap_banner_grabbing(target)

if __name__ == "__main__":
    main()