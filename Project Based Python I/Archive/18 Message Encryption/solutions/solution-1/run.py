# Source Code Link:
# https://thecleverprogrammer.com/2023/03/22/message-encryption-using-python/

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# Message
message_data = {
    "Aman": [
        {"message": "Hey Divyansha, how's it going?", "time": "2023-03-21 10:30:00"},
        {"message": "Not too bad, just working on some coding projects. Did you hear about the new encryption algorithm?", "time": "2023-03-21 10:35:00"},
        {"message": "It's called AES256 and it's supposed to be really secure. Want to give it a try with our messages?", "time": "2023-03-21 10:40:00"},
    ],
    "Divyansha": [
        {"message": "Good, thanks! How about you?", "time": "2023-03-21 10:32:00"},
        {"message": "No, what's that?", "time": "2023-03-21 10:37:00"},
        {"message": "Sure, let's do it!", "time": "2023-03-21 10:42:00"},
    ]
}
shared_secret_key = os.urandom(32)

# Encryption Function
def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message + (16 - len(message) % 16) * chr(16 - len(message) % 16)
    ciphertext = encryptor.update(padded_message.encode()) + encryptor.finalize()
    return iv + ciphertext

# Decryption Function
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    return plaintext.decode()

# Encrypting the Message
for messages in message_data.values():
    for message in messages:
        encrypted_message = encrypt_message(message["message"], shared_secret_key)
        message["message"] = encrypted_message.hex()

print("Encrypted message_data dictionary:")
print(message_data)

# Decrypting the Message
for messages in message_data.values():
    for message in messages:
        ciphertext = bytes.fromhex(message["message"])
        decrypted_message = decrypt_message(ciphertext, shared_secret_key)
        message["message"] = decrypted_message

print("\nDecrypted message_data dictionary:")
print(message_data)