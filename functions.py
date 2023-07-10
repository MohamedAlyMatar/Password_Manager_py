import re
from main import passwords

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}

def check_password_level(password):
    for level, pattern in password_patterns.items():
        if re.match(pattern, password):
            return level
    return "Unknown"

def print_colored_status(status):
    colors = {
        "weak": "\033[91m",  # Red color
        "strong": "\033[93m",  # Yellow color
        "diamond": "\033[92m",  # Green color
        "Unknown": "\033[0m"  # Reset color
    }
    color_code = colors.get(status, "")
    print("Status:", color_code + status + "\033[0m")

def get_password():
    password = input("Enter your password: ")
    level = check_password_level(password)
    print_colored_status(level)
    return password, level

def add_password():
    account = input("Enter the account name: ")
    password, level = get_password()

    if validate_password(password, level):
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
        password, level = get_password()

        if validate_password(password, level):
            passwords[account] = password
            print("Password updated successfully!")
        else:
            print("Invalid password.")
    else:
        print(f"No password found for {account}.")


def validate_password(password, level):
    if level in password_patterns:
        pattern = password_patterns[level]
        return re.match(pattern, password) is not None
    else:
        return False