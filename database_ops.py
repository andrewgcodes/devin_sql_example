import sqlite3

def get_all_users(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT username, email FROM users")
    rows = cur.fetchall()
    conn.close()
    return [{"username": r[0], "email": r[1]} for r in rows]

def get_user_details_by_name(db_path, user_name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT id, email FROM users WHERE username = '" + user_name + "'"
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "email": row[1]}
    return None

def main():
    db = "app.db"
    users = get_all_users(db)
    print("All users:", users)
    user_info = get_user_details_by_name(db, "alice")
    print("User details:", user_info)

if __name__ == "__main__":
    main()
