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
            account = input("Enter your account: ")
            password = input("Enter your password: ")
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
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
