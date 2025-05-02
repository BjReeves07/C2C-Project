from models import create_account, delete_account, login, check_balance, deposit, modify_account, withdraw
## from testFunctions import run_tests
from ui import display_menu

def main():
    print("Welcome to the Banking System")
    account = input("Enter account number: ")
    pin = input("Enter PIN: ")
    user = login(account, pin)
    
    if not user:
        print("Login failed.")
        return

    user_id, name, is_admin = user
    print(f"Welcome, {name}!")
    ##While loop to run through diferent options and print a basic UI
    while True:
        display_menu(is_admin)
        choice = input("Select an option: ")

        if choice == "1":
            print("Balance:", check_balance(user_id))
        elif choice == "2":
            amt = float(input("Amount to deposit: "))
            deposit(user_id, amt)
        elif choice == "3":
            amt = float(input("Amount to withdraw: "))
            success = withdraw(user_id, amt)
            print("Withdrawal successful" if success else "Insufficient funds.")
        elif choice == "4" and is_admin:
            name = input("Name: ")
            acc = input("New account number: ")
            pin = input("New PIN: ")
            bal = float(input("Initial balance: "))
            is_ad = input("Is admin? (y/n): ").lower() == 'y'
            create_account(name, acc, pin, bal, is_ad)
            print("Account created.")
        elif choice == "5" and is_admin:
            acc = input("Account number to delete: ")
            delete_account(acc)
            print("Account deleted.")
        elif choice == "6" and is_admin:
            acc = input("Account number to modify: ")
            name = input("New name (leave blank to skip): ") or None
            pin = input("New PIN (leave blank to skip): ") or None
            modify_account(acc, name, pin)
            print("Account modified.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
   