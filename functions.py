import re
from main import passwords

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}


def print_colored_status(status):
    colors = {
        "weak": "\033[91m",  # Red color
        "strong": "\033[93m",  # Yellow color
        "diamond": "\033[92m",  # Green color
        "Unknown": "\033[0m"  # Reset color
    }
    color_code = colors.get(status, "")
    print("Password level:", color_code + status + "\033[0m")


def validate(email):
    if re.search(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email, re.IGNORECASE):
        return True
    else:
        return False


def get_account():
    lock = True
    while lock:
        account = input("Enter your account: ")
        if validate(account):
            return account
        else:
            print("InValid email")
        

def check_password_level(password):
    for level, pattern in password_patterns.items():
        if re.match(pattern, password):
            return level
    return "Unknown"


def get_password():
    password = input("Enter your password: ")
    level = check_password_level(password)
    print_colored_status(level)
    return password


def add_password(account, password):
    if validate(account) and validate_password(password, check_password_level(password)):
        passwords[account] = password
        return "Password added successfully!"
    else:
        return "Invalid password."


def retrieve_password(account):
    if account in passwords:
        return f"Password for {account}: {passwords[account]}"
    else:
        return f"No password found for {account}."


def update_password(account, password):
    if account in passwords and validate_password(password, check_password_level(password)):
        passwords[account] = password
        return "Password updated successfully!"
    else:
        return "Invalid password."


def validate_password(password, level):
    if level in password_patterns:
        pattern = password_patterns[level]
        return re.match(pattern, password) is not None
    else:
        return False
    

def get_account_names():
    return list(passwords.keys())