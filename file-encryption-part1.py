#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os
# from cryptography.fernet import Fernet: Import the Fernet class from the cryptography library, which provides the implementation of the Fernet symmetric encryption algorithm.
# import os: Import the os module to perform operating system-related operations.


def generate_key():
    return Fernet.generate_key()
# generate_key(): A function that generates a new Fernet key using the Fernet.generate_key() method.


def load_key():
    return open("secret.key", "rb").read()
# load_key(): A function that loads the previously generated key from the "secret.key" file and returns it.

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
# save_key(key): A function that saves the provided key to the "secret.key" file in binary mode.

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)
#encrypt_file(file_path, key): A function that encrypts the contents of a file specified by file_path using the provided key and overwrites the file with the encrypted data.


def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)
# decrypt_file(file_path, key): A function that decrypts the contents of an encrypted file specified by file_path using the provided key and overwrites the file with the decrypted data.

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    print("Encrypted Message:", encrypted_message.decode())
# encrypt_message(message, key): A function that encrypts a cleartext message using the provided key and prints the resulting encrypted message.

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted Message:", decrypted_message.decode())
# decrypt_message(encrypted_message, key): A function that decrypts an encrypted message using the provided key and prints the resulting cleartext message.

def main():
    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()
#main(): The main function that serves as the entry point for the script. It checks if the "secret.key" file exists, and if not, generates a new key and saves it. Otherwise, it loads the existing key.


    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    mode = int(input("Enter mode (1-4): "))
# Print a menu for the user to select the desired mode (1-4) and prompt the user to enter the mode.

    if mode in [1, 2]:
        file_path = input("Enter file path: ")
# If the selected mode is 1 or 2, prompt the user to enter the file path.
        
    if mode == 1:
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif mode == 2:
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    elif mode == 3:
        message = input("Enter cleartext message: ")
        encrypt_message(message, key)
    elif mode == 4:
        encrypted_message = input("Enter encrypted message: ")
        decrypt_message(encrypted_message, key)
    else:
        print("Invalid mode selected.")
# Based on the selected mode, perform the corresponding operation: encrypt file, decrypt file, encrypt message, or decrypt message.

if __name__ == "__main__":
    main()
# Execute the main function if the script is run as the main module (not imported as a module).