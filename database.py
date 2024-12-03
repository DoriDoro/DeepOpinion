import sqlite3

def initialize_database():
    conn = sqlite3.connect("deep_opinion.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            result_list TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# the database is already in place, otherwise create the database with:
# initialize_database()
