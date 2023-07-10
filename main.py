import re

passwords = {}

# Regular expression patterns for different password formats
password_patterns = {
    "weak": r"^[a-zA-Z]{8,}$",
    "strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
    "diamond": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$"
}

def add_password():
    account = input("Enter the account name: ")
    password = input("Enter the password: ")

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

def menu():
    while True:
        print("\nPassword Manager")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. Update a password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            print("Thank you for using the password manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
