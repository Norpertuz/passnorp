import unittest
from unittest.mock import patch
from io import StringIO
from cryptography.fernet import Fernet
import sys
from passnorp import encrypt_data, decrypt_data, save_credentials, read_credentials, main

def generate_key():
    return Fernet.generate_key()

class TestApplication(unittest.TestCase):
    
    def test_encrypt_decrypt(self):
        key = generate_key()

        data = "Test data"
        encrypted_data = encrypt_data(data, key)
        decrypted_data = decrypt_data(encrypted_data, key)

        self.assertEqual(decrypted_data, data)


    def test_save_read_credentials(self):
        key = generate_key()


        encrypted_account = b'encrypted_account'
        encrypted_login = b'encrypted_login'
        encrypted_password = b'encrypted_password'
        filename = 'test_credentials.txt'

        save_credentials(encrypted_account, encrypted_login, encrypted_password, filename)
        credentials = read_credentials(filename)

        self.assertEqual(credentials[encrypted_account], (encrypted_login, encrypted_password))
    key = generate_key()
    @patch('builtins.input', side_effect=[key.decode(), '1', 'TestAccount', 'TestLogin', 'TestPassword', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_add_account_and_exit(self, mock_stdout, mock_input):
        filename = 'test_credentials.txt'
        main(filename)

        expected_output = "New account has been added.\nThat's enough.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
