from functions import *

passwords = {}

def menu():
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
            add_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            account_names = get_account_names()
            print("Account names:", account_names)
        elif choice == "5":
            print("Thank you for using the password manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
