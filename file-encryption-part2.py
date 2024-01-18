#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key", "rb").read()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    print("Encrypted Message:", encrypted_message.decode())

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted Message:", decrypted_message.decode())

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key)

def main():
    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Encrypt a folder and its contents")
    print("6. Decrypt a folder encrypted by this tool")

    mode = int(input("Enter mode (1-6): "))

    if mode in [1, 2]:
        file_path = input("Enter file or folder path: ")
        
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
    elif mode == 5:
        encrypt_folder(file_path, key)
        print("Folder and its contents encrypted successfully.")
    elif mode == 6:
        decrypt_folder(file_path, key)
        print("Folder and its contents decrypted successfully.")
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()