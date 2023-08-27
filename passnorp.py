from cryptography.fernet import Fernet
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
def save_credentials(login, encrypted_password, filename):
    with open(filename, 'ab') as file:
        line =f"{login}:{encrypted_password}\n"
        file.write(line.encode())

# Reading encrypted data from file
def read_credentials(filename):
    credentials = {}
    with open(filename, 'rb') as file:
        for line in file:
            login, encrypted_password = line.decode().strip().split(':')
            credentials[login] = encrypted_password
    return credentials

# Main function with main loop
def main():
    key = input("Enter key: ").strip()
    credentials = read_credentials('credentials.txt')
    
    #Deleting unexpected b prefix
    if key.startswith("b'") and key.endswith("'"):
        key = key[2:-1]

    while True:
        print("Menu:")
        print("1. Add new password")
        print("2. Show all passwords")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            login = input("Enter login: ")
            password = input("Enter new password: ")
            encrypted_password = encrypt_data(password, key)
            credentials[login] = encrypted_password
            save_credentials(login, encrypted_password, 'credentials.txt')
            print("New password has been added.")

        elif choice == "2":
            for login, encrypted_password in credentials.items():
                decrypted_password = decrypt_data(encrypted_password, key)
                print(f"Login: {login}, Decrypted password:  {decrypted_password}")

        elif choice == "3":
            print("That's enough.")
            break

if __name__ == "__main__":
    if not os.path.exists('credentials.txt'):
        with open('credentials.txt', 'w') as file:
            pass #Touching new file if not exists

    main()
