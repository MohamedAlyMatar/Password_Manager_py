from functions import *

passwords = {}

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
