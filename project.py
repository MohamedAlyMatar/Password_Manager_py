import re

passwords = {}

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}


# password level colors
def print_colored_status(status):
    colors = {
        "weak": "\033[91m",    # Red color
        "strong": "\033[93m",  # Yellow color
        "diamond": "\033[92m", # Green color
        "Unknown": "\033[0m"   # Reset color
    }
    color_code = colors.get(status, "")
    print("Password level:", color_code + status + "\033[0m")


# function to validate the user email input
def validate(email):
    if re.search(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email, re.IGNORECASE):
        return True
    else:
        return False


# function to get the account from the user and validate it
def get_account():
    lock = True
    while lock:
        account = input("Enter your account: ")
        if validate(account):
            return account
        else:
            print("InValid email")


def validate_password(password, level):
    # Check if the password matches the given level's pattern
    if level in password_patterns:
        pattern = password_patterns[level]
        return re.match(pattern, password) is not None
    else:
        return False


# function to validate password and check its level
def check_password_level(password):
    # Iterate over the password patterns and check if the password matches any level
    for level, pattern in password_patterns.items():
        if re.match(pattern, password):
            return level
    return "Unknown"


# function to get the password
def get_password():
    password = input("Enter your password: ")
    level = check_password_level(password)
    print_colored_status(level)
    return password

# functionality 1: add password
def add_password(account, password):
    # Check if the account and password are valid before adding the password
    if validate(account) and validate_password(password, check_password_level(password)):
        passwords[account] = password
        return "Password added successfully!"
    else:
        return "Invalid password."


# functionality 2: retrieve password
def retrieve_password(account):
    if account in passwords:
        return f"Password for {account}: {passwords[account]}"
    else:
        return f"No password found for {account}."


# functionality 3: update password
def update_password(account, password):
    # Check if the account exists and if the new password is valid before updating
    if account in passwords and validate_password(password, check_password_level(password)):
        passwords[account] = password
        return "Password updated successfully!"
    else:
        return "Invalid password."


# functionality 4: get all email accounts
def get_account_names():
    # Return a list of account names
    return list(passwords.keys())


def main():
    while True:
        print("\n ---- Welcome to your Password Manager ---- ")
        print(" | 1. Add a password                       | ")
        print(" | 2. Retrieve a password                  | ")
        print(" | 3. Update a password                    | ")
        print(" | 4. Get all accounts                     | ")
        print(" | 5. Exit                                 | ")
        print(" ------------------------------------------- ")
        choice = input(" -> Enter your choice (1-5): ")
        print(" ------------------------------------------- ")

        if choice == "1":
            account = get_account()
            password = get_password()
            result = add_password(account, password)
            print(result)

        elif choice == "2":
            account = input("Enter the account name: ")
            result = retrieve_password(account)
            print(result)

        elif choice == "3":
            account = input("Enter the account name: ")
            password = input("Enter your new password: ")
            result = update_password(account, password)
            print(result)

        elif choice == "4":
            accounts = get_account_names()
            if len(accounts) == 0:
                print("No accounts found.")
            else:
                print("List of accounts:")
                for account in accounts:
                    print(account)

        elif choice == "5":
            print("Thanks for using our password manager :)")
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
