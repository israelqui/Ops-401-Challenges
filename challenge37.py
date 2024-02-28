#!/usr/bin/env python3
# Script Name: Cookie Capture Capades 
# Description: Python script that will capture a cookie and send it back out to the site in order to receive a valid response in HTTP text, all using Python’s Requests module.
# Author: Israel Quirola
# Date: February 27, 2024

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
# This line imports the webbrowser module, which provides a high-level interface to display web-based documents to users. It allows us to open web pages in the default web browser.
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above

# This line sends an HTTP GET request to the targetsite URL using the requests.get() function. It returns a Response object containing the response from the server, including headers, status code, and content.
response = requests.get(targetsite)

# This line retrieves the cookies sent by the server in the response and assigns them to the variable cookie. 
cookie = response.cookies

# This line defines a function named bringforthcookiemonster. Functions in Python are defined using the def keyword followed by the function name and parentheses.
def bringforthcookiemonster(): # Because why not!
    
    # This block of code is a multi-line string that represents an ASCII art of Cookie Monster. It's printed when the bringforthcookiemonster function is called.
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

# This line defines a function named send_cookie_and_capture_response that takes two parameters: targetsite (the URL of the target site) and cookie (the cookie to send with the request).
def send_cookie_and_capture_response(targetsite, cookie):
    
    # This line prints a message indicating that the script is sending the cookie back to the site.
    print("Sending cookie back to the site...")

    # This line sends an HTTP GET request to the targetsite URL, including the cookie in the request headers. It assigns the response to the response variable.
    response = requests.get(targetsite, cookies=cookie)

    # This line prints the status code of the HTTP response received from the server.
    print("Received HTTP response with status code:", response.status_code)

    # This line retrieves the HTML content of the response and assigns it to the variable html_content.
    html_content = response.text

    # This block of code opens a file named response.html in write mode and writes the HTML content to it. It uses a with statement to automatically close the file after writing.
    with open("response.html", "w") as html_file:
        html_file.write(html_content)

    # This line prints a message indicating that the HTML response has been saved to the file response.html.    
    print("HTML response saved to response.html")

# This line defines a function named open_in_firefox that takes one parameter: html_file (the path to the HTML file to open).
def open_in_firefox(html_file):
    print("Opening HTML response in Firefox...")

    # This line opens the specified HTML file (html_file) in Firefox using the webbrowser.get("firefox").open() function.
    webbrowser.get("firefox").open(html_file)

# This line defines a function named main. This function serves as the entry point of the script.
def main():
    
    # This line calls the bringforthcookiemonster function to print the ASCII art of Cookie Monster.
    bringforthcookiemonster()

    # This line prints a message indicating the target site URL.
    print("Target site is " + targetsite)

    # This line prints the cookie that was retrieved from the server's response.
    print("Cookie:", cookie)

    # This line calls the send_cookie_and_capture_response function to send the cookie back to the site and capture the response.
    send_cookie_and_capture_response(targetsite, cookie)

    # This line calls the open_in_firefox function to open the generated HTML file in Firefox.
    open_in_firefox("response.html")

# This line checks if the script is being run directly (not imported as a module) and then calls the main function. This allows the script to be reusable as a module if needed.
if __name__ == "__main__":
    main()

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands