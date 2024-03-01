from cryptography.fernet import Fernet
import os.path

def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Check if key file exists, if not, generate it
if not os.path.isfile("key.key"):
    writeKey()

masterPassword = input("Enter your master password: ")
key = loadKey() + masterPassword.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(":")
            print("user:", user, ", password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("Enter your account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(f"{name}: {fer.encrypt(pwd.encode()).decode()}\n")

mode = input("Would you like to add a new password or view the old ones? (Press 'Q' to Quit)").lower()

while True:
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
    mode = input("Would you like to add a new password or view the old ones? (Press 'Q' to Quit)").lower()
