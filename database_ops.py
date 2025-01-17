import sqlite3

def get_all_users(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT username, email FROM users")
    rows = cur.fetchall()
    conn.close()
    return [{"username": r[0], "email": r[1]} for r in rows]

def main():
    db = "app.db"
    users = get_all_users(db)
    print("All users:", users)

if __name__ == "__main__":
    main()
