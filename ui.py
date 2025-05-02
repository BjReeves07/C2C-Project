def display_menu(is_admin=False):
    ##Didn't have time to set up a full GUI with PyQt5 due to school so resorted to a basic userface in the terminal with print statements.
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    if is_admin:
        print("4. Create Account")
        print("5. Delete Account")
        print("6. Modify Account")
    print("0. Exit")