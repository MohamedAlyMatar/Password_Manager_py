import re
from main import passwords

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}

def add_password():
    account = input("Enter account name: ")
    password = input("Enter password: ")

    if validate_password(password):
        passwords[account] = password
        print("Password added successfully!")
    else:
        print("Invalid password.")

def retrieve_password():
    account = input("Enter the account name: ")

    if account in passwords:
        print(f"Password for {account}: {passwords[account]}")
    else:
        print(f"No password found for {account}.")

def update_password():
    account = input("Enter the account name: ")

    if account in passwords:
        password = input("Enter the new password: ")

        if validate_password(password):
            passwords[account] = password
            print("Password updated successfully!")
        else:
            print("Invalid password.")
    else:
        print(f"No password found for {account}.")

def validate_password(password):
    for pattern_name, pattern in password_patterns.items():
        if re.match(pattern, password):
            return True
    return False