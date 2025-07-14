import csv
import sqlite3

CSV_FILE = 'students.csv'
DB_FILE = 'school.db'

def load_csv():
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except:
        print("CSV load error")

def add_student():
    name = input("Name: ")
    roll = input("Roll Number: ")
    grade = input("Grade: ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, roll_number, grade) VALUES (?, ?, ?)", (name, roll, grade))
    conn.commit()
    conn.close()
    print("Student added.")

def search_student():
    roll = input("Enter roll to search: ")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll,))
    print(cursor.fetchone())
    conn.close()

def update_student():
    roll = input("Roll to update: ")
    grade = input("New Grade: ")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE roll_number = ?", (grade, roll))
    conn.commit()
    conn.close()
    print("Updated.")

def delete_student():
    roll = input("Roll to delete: ")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll,))
    conn.commit()
    conn.close()
    print("Deleted.")

if __name__ == '__main__':
    print("1. Load CSV")
    print("2. Add Student")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    choice = input("Enter choice: ")
    if choice == '1':
        load_csv()
    elif choice == '2':
        add_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
