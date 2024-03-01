# Simple Password Manager

This is a simple password manager written in Python using the Fernet encryption library from `cryptography` module. This manager allows users to store and view their passwords securely.

## How It Works

- The script generates a random encryption key using Fernet and saves it to a file named `key.key`.
- Users can then add new passwords or view existing ones.
- Each password is encrypted using the generated key along with a master password provided by the user during runtime.
- Passwords are stored in a file named `password.txt` in the format `username: encrypted_password`.

## Setup

1. **Install Dependencies**: Ensure you have Python installed on your system along with the `cryptography` library. You can install it using pip:

    ```
    pip install cryptography
    ```

2. **Run the Script**: Execute the script `password_manager.py`:

    ```
    python password_manager.py
    ```

3. **Usage**: Follow the prompts to add or view passwords. You can press 'Q' to quit at any time.

## Features

- **Encryption**: Passwords are encrypted using Fernet encryption, ensuring they are stored securely.
- **Master Password**: Each password is encrypted using a master password provided by the user, adding an extra layer of security.
- **Add or View Passwords**: Users can add new passwords or view existing ones with ease.
- **Simple Interface**: The script provides a simple command-line interface for managing passwords.

## Note

- Make sure to remember your master password. Without it, you won't be able to decrypt your passwords.
- Keep the `key.key` file safe. Losing this file will make it impossible to decrypt your passwords.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
