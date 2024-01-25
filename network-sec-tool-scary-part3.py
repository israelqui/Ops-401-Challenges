#!/usr/bin/env python3
# Script Name: TCP Port Range Scanner Part 3
# Description: This script will Ping an IP address determined by the user. If the host exists, scan its ports and determine if any are open.
# Author: Israel Quirola
# Date: January 25, 2024

from scapy.all import TCP, IP, sr1, ICMP

def port_scan(target_ip, port_range):
    print(f"Scanning ports for {target_ip}...\n")

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

def network_scanner(ip_address):
    # ICMP ping to check if the host is responsive
    icmp_packet = IP(dst=ip_address) / ICMP()
    response = sr1(icmp_packet, timeout=1, verbose=0)

    if response:
        # Host is responsive, perform port scan
        print(f"\nHost {ip_address} is responsive to ICMP echo requests.")
        port_range = tuple(map(int, input("Enter the port range (start end): ").split()))
        port_scan(ip_address, port_range)
    else:
        # No response, host is down or unresponsive
        print(f"\nHost {ip_address} is down or unresponsive.")

# Prompt the user for an IP address to target
target_ip = input("Enter the target IP address: ")

# Call the network scanner function
network_scanner(target_ip)