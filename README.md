<div align="center">
    <p>🔐 Encrypted Password Manager</p>
</div>


This is a simple password manager built with Python that uses the cryptography library to securely store passwords using Fernet symmetric encryption.

<br>

📦 Features

<br>

    🔐 Password Encryption using a unique key (Fernet).

    ➕ Add new encrypted passwords.

    👀 View decrypted passwords.

    💾 Local Storage in a .txt file.

<br>

⚙️ Prerequisites

<br>

    Python 3.6+

    cryptography library

Install the library using pip:
Bash

pip install cryptography

<br>

🚀 How to Use

<br>

1. Generate the Encryption Key

Before running the program, you must generate the key used to encrypt and decrypt passwords. Uncomment the following snippet in the code and run it once:
Python

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

This will create a key.key file, which will be required for subsequent runs.
2. Run the Program

After generating the key, comment out the write_key() snippet and run the program normally:
Bash

python main.py

You will see the following menu:
Plaintext

Would you like to add a new password, view existing ones or quit? (add/view/quit)?

add: Adds a new account and password.
view: Displays all accounts with their decrypted passwords.
quit: Exits the program.

<br>

📁 File Structure

<br>

    main.py: The main application code.

    key.key: The generated encryption key (NEVER share this file publicly).

    passwords.txt: The file where passwords are stored in encrypted format.

<br>

🛡️ Security Disclaimer

<br>

This project is for educational purposes only. Do not use this manager to store real or sensitive passwords, as it lacks protection against physical file access and advanced security management.

<br>

🧠 Key Learnings

<br>

This project demonstrates:

    File handling (reading/writing) with Python.

    Symmetric encryption using Fernet.

    Terminal-based menu structures.

<br>

📄 License

<br>

This project is licensed under the MIT License. Feel free to use, modify, and share.
