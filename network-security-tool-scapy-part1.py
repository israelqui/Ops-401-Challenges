#!/usr/bin/env python3

from scapy.all import *

def tcp_port_scanner(target_ip, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        # Crafting the TCP SYN packet
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(dport=port, flags="S")
        packet = ip_packet / tcp_packet

        # Sending the packet and receiving the response
        response = sr1(packet, timeout=1, verbose=0)

        if response:
            # Check the TCP flags in the response
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                # If flag 0x12 received, send a RST packet to close the connection
                send(IP(dst=target_ip) / TCP(dport=port, flags="R"), verbose=0)
                print(f"Port {port} is open")
            elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                # If flag 0x14 received, notify the user the port is closed
                print(f"Port {port} is closed")
            else:
                # If no flag is received, notify the user the port is filtered and silently dropped
                print(f"Port {port} is filtered and silently dropped")
        else:
            # If no response received, consider the port closed
            print(f"Port {port} is closed")

# Define the target host IP and port range
target_ip = "192.168.1.1"
port_range = (1, 100)

# Call the scanner function
tcp_port_scanner(target_ip, port_range)