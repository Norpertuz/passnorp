from cryptography.fernet import Fernet

# Szyfrowanie danych
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Deszyfrowanie danych
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Zapisywanie zaszyfrowanych danych do pliku
def save_encrypted_data(data, filename):
    with open(filename, 'ab') as file:
        file.write(data)

# Odczytywanie zaszyfrowanych danych z pliku
def read_encrypted_data(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

# Główna funkcja programu
def main():
    key = input("Podaj klucz: ").encode()

    while True:
        print("Menu:")
        print("1. Dodaj nowe hasło")
        print("2. Wyświetl hasła")
        print("3. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            password = input("Podaj nowe hasło: ")
            encrypted_password = encrypt_data(password, key)
            save_encrypted_data(encrypted_password, 'passwords.txt')
            print("Hasło zostało dodane.")

        elif choice == "2":
            encrypted_passwords = read_encrypted_data('passwords.txt')
            decrypted_passwords = decrypt_data(encrypted_password, key)
            print("Odszyfrowane hasło:", decrypted_password)

        elif choice == "3":
            print("Koniec programu.")
            break

if __name__ == "__main__":
    main()
