#!/usr/bin/env python3
# Script Name: TCP Port Range Scanner Part 2
# Description: This script uses Scapy to Generating a Range of IP Addresses from a CIDR Address in Python
# Author: Israel Quirola
# Date: January 24, 2024

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

def icmp_ping_sweep(network_address):
    # Create a list of all addresses in the given network (excluding network and broadcast addresses)
    ip_addresses = [str(ip) for ip in IP(network_address).hosts()]

    # Initialize counters
    online_count = 0
    blocking_count = 0

    for ip_address in ip_addresses:
        # Skip network and broadcast addresses
        if IP(ip_address).dst == network_address or IP(ip_address).dst == IP(network_address).broadcast:
            continue

        # Crafting the ICMP Echo Request packet
        icmp_packet = IP(dst=ip_address) / ICMP()
        response = sr1(icmp_packet, timeout=1, verbose=0)

        if response:
            # Check ICMP type and code in the response
            if response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
                # Host actively blocking ICMP traffic
                print(f"Host {ip_address} is actively blocking ICMP traffic.")
                blocking_count += 1
            else:
                # Host is responding
                print(f"Host {ip_address} is responding.")
                online_count += 1
        else:
            # No response, host is down or unresponsive
            print(f"Host {ip_address} is down or unresponsive.")

    # Inform the user about the total number of hosts online and actively blocking ICMP traffic
    print(f"\nTotal online hosts: {online_count}")
    print(f"Total hosts actively blocking ICMP traffic: {blocking_count}")

# User menu
print("1. TCP Port Range Scanner mode")
print("2. ICMP Ping Sweep mode")
user_choice = input("Enter your choice (1 or 2): ")

if user_choice == '1':
    # TCP Port Range Scanner mode
    target_ip = input("Enter the target IP address: ")
    port_range = tuple(map(int, input("Enter the port range (start end): ").split()))
    tcp_port_scanner(target_ip, port_range)

elif user_choice == '2':
    # ICMP Ping Sweep mode
    network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
    icmp_ping_sweep(network_address)

else:
    print("Invalid choice. Please enter 1 or 2.")