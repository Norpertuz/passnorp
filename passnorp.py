#!/usr/bin/env python3
from cryptography.fernet import Fernet
from colorama import init, Fore, Style
import os

# Data encryption
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Data decryption
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Saving encrypted data to file in append mode
def save_credentials(encrypted_account, encrypted_login, encrypted_password, filename):
    with open(filename, 'ab') as file:
        line =f"{encrypted_account.decode()}:{encrypted_login.decode()}:{encrypted_password.decode()}\n"
        file.write(line.encode())

# Reading encrypted data from file
def read_credentials(filename):
    credentials = {}
    with open(filename, 'rb') as file:
        for line in file:
            encrypted_account, encrypted_login, encrypted_password = line.strip().split(b':')
            credentials[encrypted_account] = (encrypted_login, encrypted_password)
    return credentials

# Main function with main loop
def main(credentials_file_path):
    key = input("Enter key: ").strip()

    credentials = read_credentials(credentials_file_path)
    
    #Deleting unexpected b prefix
    if key.startswith("b'") and key.endswith("'"):
        key = key[2:-1]

    while True:
        print("Menu:")
        print("1. Add new account")
        print("2. Show all accounts")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            account = input("Enter account: ")
            login = input("Enter login: ")
            password = input("Enter password: ")
            encrypted_password = encrypt_data(password, key)
            encrypted_account = encrypt_data(account, key)
            encrypted_login = encrypt_data(login, key)
            credentials[encrypted_account] = (encrypted_login, encrypted_password)
            save_credentials(encrypted_account, encrypted_login, encrypted_password, credentials_file_path)
            print("New account has been added.")

        elif choice == "2":
            #terminal_width = os.get_terminal_size().columns
            print(Fore.LIGHTRED_EX + "{:<40}{:<40}{:<40}".format("Account", "Login", "Password"))
            print("="*100)
            for encrypted_account, (encrypted_login, encrypted_password) in sorted(read_credentials(credentials_file_path).items(), key=lambda item: decrypt_data(item[0], key).lower()):
                decrypted_account = decrypt_data(encrypted_account, key)
                decrypted_login = decrypt_data(encrypted_login, key)
                decrypted_password = decrypt_data(encrypted_password, key)
                #print(f"Account: {decrypted_account}, Login: {decrypted_login}, Password:  {decrypted_password}")
                print(Fore.YELLOW + "{:<40}{:<40}{:<40}".format(decrypted_account, decrypted_login, decrypted_password) + Style.RESET_ALL)
        elif choice == "3":
            print("That's enough.")
            break

if __name__ == "__main__":
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    credentials_file_path = os.path.join(current_directory, 'credentials.txt')
    if not os.path.exists(credentials_file_path):
        with open(credentials_file_path, 'w') as file:
            pass #Touching new file if not exists

    main(credentials_file_path)
