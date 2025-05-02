from db import connect_db

# Function to handle user login by checking account number and pin
def login(account_number, pin):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    query = "SELECT id, name, is_admin FROM bank.bankusers WHERE account_number=%s AND pin=%s"
    cursor.execute(query, (account_number, pin))
    user = cursor.fetchone()
    conn.close()
    return user  # None if login fails

# Retrieves the user's balance from the database using their user ID
def check_balance(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    cursor.execute("SELECT balance FROM bank.bankusers WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


# Adds a specified amount to the user's balance
def deposit(user_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    cursor.execute("UPDATE bank.bankusers SET balance = balance + %s WHERE id = %s", (amount, user_id))
    conn.commit()
    conn.close()

# Withdraws a specified amount from the user's balance if enough funds are available
def withdraw(user_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    cursor.execute("SELECT balance FROM bank.bankusers WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        cursor.execute("UPDATE bank.bankusers SET balance = balance - %s WHERE id = %s", (amount, user_id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
# Creates a new user account with the provided details (name, account number, etc.)
def create_account(name, account_number, pin, balance, is_admin):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    cursor.execute(
        "INSERT INTO bank.bankusers (name, account_number, pin, balance, is_admin) VALUES (%s, %s, %s, %s, %s)",
        (name, account_number, pin, balance, is_admin)
    )
    conn.commit()
    conn.close()


# Deletes a user account based on the account number
def delete_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    cursor.execute("DELETE FROM bank.bankusers WHERE account_number = %s", (account_number,))
    conn.commit()
    conn.close()


# Updates a user's account (name or pin) based on the given account number
def modify_account(account_number, name=None, pin=None):
    conn = connect_db()
    cursor = conn.cursor()
    # Update the query to reference the correct schema and table
    if name:
        cursor.execute("UPDATE bank.bankusers SET name = %s WHERE account_number = %s", (name, account_number))
    if pin:
        cursor.execute("UPDATE bank.bankusers SET pin = %s WHERE account_number = %s", (pin, account_number))
    conn.commit()
    conn.close()