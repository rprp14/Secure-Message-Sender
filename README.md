# Secure-Message-Sender
# Secure Message Sender

Secure Message Sender is a Python-based project that encrypts messages using the `cryptography` library and sends them via email along with their decrypted versions as attachments. This ensures the secure transmission of sensitive information.

## Features
- Encrypt plain text messages using `Fernet` symmetric encryption.
- Save encrypted messages to a file for later use.
- Decrypt encrypted messages and save the output to a file.
- Send both the encrypted and decrypted message files as email attachments.
- Simple and efficient implementation with Python.

## Requirements
- Python 3.x
- `cryptography` library
- `smtplib` (built-in Python library)
- Gmail account with App Password enabled

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/secure-message-sender.git
