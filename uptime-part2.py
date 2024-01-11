#!/usr/bin/env python3

import time
import subprocess
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def send_notification(sender_email, sender_password, receiver_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:  # Replace with your SMTP server and port
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Error sending notification: {e}")

def monitoring():
    # Get user input for email and password
    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")
    receiver_email = input("Enter the administrator's email address: ")

    # Initialize the previous status as 'Up'
    previous_status = True

    while True:
        ip = input("Enter an IP address to monitor (or 'quit' to exit): ")
        
        if ip.lower() == 'quit':
            break
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        current_status = (result.returncode == 0)

        if current_status != previous_status:
            # Status changed, send notification
            status_change_message = f"Host status changed at {timestamp}.\n"\
                                    f"Previous Status: {'Connection Active' if previous_status else 'Connection Deactivated'}\n"\
                                    f"Current Status: {'Connection Active' if current_status else 'Connection Deactivated'}\n"\
                                    f"IP Address: {ip}"

            send_notification(sender_email, sender_password, receiver_email, "Host Status Change", status_change_message)

        print(f"{timestamp} {'Connection Active' if current_status else 'Connection Deactivated'} to {ip}")

        previous_status = current_status
        time.sleep(2)

if __name__ == "__main__":
    monitoring()