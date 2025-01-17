import sqlite3
from typing import Optional, Dict, Union, List

def get_all_users(db_path: str) -> List[Dict[str, Union[str]]]:
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT username, email FROM users")
        rows = cur.fetchall()
    return [{"username": r[0], "email": r[1]} for r in rows]

def get_user_details_by_name(db_path: str, user_name: str) -> Optional[Dict[str, Union[int, str]]]:
    """Retrieve user details from the database by username.

    Args:
        db_path: Path to the SQLite database file
        user_name: Username to look up

    Returns:
        Dictionary containing user id and email if found, None otherwise
    """
    query = "SELECT id, email FROM users WHERE username = ?"
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(query, (user_name,))
        row = cur.fetchone()
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
