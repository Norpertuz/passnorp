from cryptography.fernet import Fernet

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
def save_encrypted_data(data, filename):
    with open(filename, 'ab') as file:
        file.write(data)

# Reading encrypted data from file
def read_encrypted_data(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

# Main function with main loop
def main():
    key = input("Enter key: ").strip()
    
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
            password = input("Enter new password: ")
            encrypted_passwords = encrypt_data(password, key)
            save_encrypted_data(encrypted_passwords, 'passwords.txt')
            print("New password has been added.")

        elif choice == "2":
            encrypted_passwords = read_encrypted_data('passwords.txt')
            decrypted_passwords = decrypt_data(encrypted_passwords, key)
            print("Decrypted data: ", decrypted_passwords)

        elif choice == "3":
            print("That's enough.")
            break

if __name__ == "__main__":
    main()
