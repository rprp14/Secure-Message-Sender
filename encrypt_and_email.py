'''import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate a key and instantiate a Fernet cipher
def generate_key():
    return Fernet.generate_key()

# Function to encrypt the message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to send email
def send_email(receiver_email, subject, body):
    sender_email = "pranjalibodke14@gmail.com"  # Replace with your email
    password = "cgjf yfav jpjm lkry"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    # Read the plain text message from a file
    with open('message.txt', 'r') as file:
        plain_text = file.read()

    # Generate a key and encrypt the message
    key = generate_key()
    encrypted_message = encrypt_message(plain_text, key)

    # Save the encrypted message to a file
    with open('encrypted_message.txt', 'wb') as file:
        file.write(encrypted_message)

    # Send the encrypted message via email
    receiver_email = "pranjalibodke70@gmail.com"  # Replace with receiver's email
    subject = "Encrypted Message"
    body = f"Here is the encrypted message:\n\n{encrypted_message.decode()}\n\nKey (keep it secret): {key.decode()}"
    send_email(receiver_email, subject, body)

if __name__ == "__main__":
    main()'''

import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Function to generate a key and instantiate a Fernet cipher
def generate_key():
    return Fernet.generate_key()

# Function to encrypt the message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to decrypt the message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to send email with attachments
def send_email_with_attachments(receiver_email, subject, body, files):
    sender_email = "pranjalibodke14@gmail.com"  # Replace with your email
    password = "cgjf yfav jpjm lkry"  # Replace with your app password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach each file
    for file_path in files:
        with open(file_path, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}",
        )
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email with attachments sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    # Read the plain text message from a file
    with open('message.txt', 'r') as file:
        plain_text = file.read()

    # Generate a key and encrypt the message
    key = generate_key()
    encrypted_message = encrypt_message(plain_text, key)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)

    # Save the encrypted message to a file
    with open('encrypted_message.txt', 'wb') as file:
        file.write(encrypted_message)

    # Save the decrypted message to a file
    with open('decrypted_message.txt', 'w') as file:
        file.write(decrypted_message)

    # Send the encrypted and decrypted messages as attachments via email
    receiver_email = "pranjalibodke70@gmail.com"  # Replace with receiver's email
    subject = "Encrypted and Decrypted Messages"
    body = (
        "Attached are the encrypted and decrypted messages.\n"
        "Keep the key secret for decrypting the message."
    )
    files = ['encrypted_message.txt', 'decrypted_message.txt']
    send_email_with_attachments(receiver_email, subject, body, files)

if __name__ == "__main__":
    main()
