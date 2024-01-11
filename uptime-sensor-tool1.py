#!/usr/bin/env python3

import time
import subprocess
from datetime import datetime
# import time: Imports the time module, which provides various time-related functions.
# import subprocess: Imports the subprocess module, enabling the execution of system commands from Python.
# from datetime import datetime: Imports the datetime class from the datetime module. This will be used to generate timestamps for the output.

def monitoring(ips):# def check_hosts_status(ips):: Defines a function named check_hosts_status that takes a list of IP addresses (ips) as an argument.
    while True:#while True:: Starts an infinite loop that continuously monitors the specified IP addresses.
        for ip in ips:#for ip in ips:: Initiates a loop through each IP address in the ips list.
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")#timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"): Generates a timestamp using datetime.now() and formats it as a string with year, month, day, hour, minute, second, and microsecond.
            result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)#result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL): Executes the ping command for the current IP address (ip). -c 1 specifies sending only one ICMP packet. subprocess.DEVNULL redirects the output and errors to null, suppressing the command output.
            if result.returncode == 0:
                status = "Conexion Activa"
            else:
                status = "Conexion Desactivada"
                #if result.returncode == 0:: Checks the return code of the ping command. A return code of 0 indicates a successful ICMP response.
                #status = "Conexion Activa" and status = "Conexion Desactivada": Sets the status variable based on the return code. If the return code is 0, it considers the network as active; otherwise, it considers it inactive.
            print(f"{timestamp} {status} to {ip}")
        time.sleep(2)  # Wait for 2 seconds before sending the next ICMP packet

ips_to_ping = ['8.8.8.8', '10.0.1.0', 'google.com']
monitoring(ips_to_ping)