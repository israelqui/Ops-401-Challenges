#!/usr/bin/env python3
# Script Name: Create a Port Scanner
# Description: The socket python module grants us access to low level networking interface operations directly from the Python 3 script.
# Author: Israel Quirola
# Date: March 06, 2024

import socket

# Create a socket object with IPv4 addressing and TCP protocol
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout for the socket operations (in seconds)
timeout = 5  # You can set any appropriate value for the timeout here
sockmod.settimeout(timeout)

# Collect host IP address from the user
hostip = input("Enter the host IP address: ")

# Collect port number from the user and convert it to an integer data type
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        # Attempt to connect to the specified host and port
        sockmod.connect((hostip, portno))
        # If connection is successful, the port is open
        print("Port open")
    except socket.error:
        # If an error occurs (connection fails), the port is closed
        print("Port closed")
    finally:
        # Close the socket connection
        sockmod.close()

# Call the portScanner function with the provided port number
portScanner(portno)