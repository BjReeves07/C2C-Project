from models import login, check_balance, deposit, withdraw
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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()