from crypto import encrypt, decrypt

def main():
    # Define passphrase to encrypt and decrypt messages.
    passphrase = 'SomeStrongPassword'

    # Some random message.
    message = 'This is a private message!'

    # Encrypt message.
    encrypted_message = encrypt(message, passphrase)
    
    # Decrypt encrypted message. 
    decrypted_message = decrypt(encrypted_message, passphrase)
    
    print(f'Encrypted message: {encrypted_message}')
    print(f'Decrypted message: {decrypted_message}')

if __name__ == '__main__':
    main()
