##Visual Studio was being weird and only allowed the python to run with the main.py function, so I am unsure if this testing works.

from models import login, check_balance, deposit, withdraw, create_account, delete_account

def test_login():
    from models import login
    user = login("000001", "9834")  # Account and pin together based on the table made with SQL
    assert user is not None, "Login failed when it should have succeeded"
    print("test_login passed")


def test_balance():
    from models import check_balance
    balance = check_balance(2)  # Replace with a valid user_id
    assert balance is not None, "Balance check failed"
    print("test_balance passed")


def test_deposit():
    from models import deposit, check_balance
    user_id = 2  # Replace with a valid user_id
    initial = check_balance(user_id)
    deposit(user_id, 100)
    after = check_balance(user_id)
    assert after == initial + 100, "Deposit failed"
    print("test_deposit passed")


def test_withdraw():
    from models import withdraw, check_balance
    user_id = 1  # Replace with a valid user_id
    deposit(user_id, 50)  # Make sure there's enough to withdraw
    initial = check_balance(user_id)
    success = withdraw(user_id, 50)
    after = check_balance(user_id)
    assert success, "Withdraw failed"
    assert after == initial - 50, "Withdraw did not reduce balance"
    print("test_withdraw passed")


# Make sure the tests actually run:
if __name__ == "__main__":
    test_login()
    test_balance()
    test_deposit()
    test_withdraw()

print("Code is running")