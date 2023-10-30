<img src="./images/message-encryption.png" width="700"/>

# Message Encryption
> DIFFICULTY: **INTERMEDIATE**

Message encryption means keeping the message secret. In simple words, Message Encryption means putting the message in a secret box that only the receiver can open.
Fore message encryption using Python, you need to have a library installed in your system known as **cryptography**.

The conversation between two people can be a dictionary as follows:
```python
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
```

## TODO

1. Define the message_data
2. Define a secret key
3. Write Encryption Function
4. Write Decryption Function
5. Encrypt the Message
6. Decrypt the Message
