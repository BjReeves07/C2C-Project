from db import connect_db

def login(account_number, pin):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT id, name, is_admin FROM users WHERE account_number=%s AND pin=%s"
    cursor.execute(query, (account_number, pin))
    user = cursor.fetchone()
    conn.close()
    return user  # None if login fails

def check_balance(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def deposit(user_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, user_id))
    conn.commit()
    conn.close()

def withdraw(user_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False