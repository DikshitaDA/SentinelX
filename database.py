import sqlite3

DB_NAME="sentinelx.db"

def get_connection():
    conn=sqlite3.connect(DB_NAME)
    conn.row_factory=sqlite3.Row
    return conn

def create_logs_table():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS logs(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   ip_address TEXT,
                   endpoint TEXT,
                   timestamp TEXT
                   )
                   """)
    conn.commit()
    conn.close()