import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('school.db')
        print("Database connection established")
        return conn
    except Error as e:
        print(f"Database error: {e}")
        return None

def init_db():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    roll_number TEXT UNIQUE NOT NULL,
                    grade TEXT NOT NULL
                )
            """)
            conn.commit()
            print("Students table created")
        except Error as e:
            print(f"Table creation error: {e}")
        finally:
            conn.close()