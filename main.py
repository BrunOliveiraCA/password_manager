# IMPORTS
from cryptography.fernet import Fernet


# GENERATING A KEY FILE FOR ENCRYPTION

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


# LOADING THE KEY OF THE ENCRYPTION


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()

fer = Fernet(key)

# FUNCTION TO ADD A NEW USER


def add():
    acc = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(acc + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# FUNCTION TO VIEW ALL THE PASSWORDS


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(
                f"""
                Username: {user}
                Password: {fer.decrypt(passw.encode()).decode()}
            """
            )


# USER'S MENU

while True:
    mode = input(
        "Would you like to add a new password, view existing ones or quit? (add/view/quit)? "
    ).lower()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "quit":
        break
    else:
        print("Invalid mode.")
        continue
