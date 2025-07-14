import sqlite3

def create_students_table():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT UNIQUE NOT NULL,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Students table created successfully.")

