import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ho TEXT,
        ten TEXT,
        email TEXT,
        password TEXT,
        ngay_sinh TEXT,
        gioi_tinh TEXT
    )
    """)

    conn.commit()
    conn.close()