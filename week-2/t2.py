from flask import Blueprint, request, jsonify
import sqlite3

student_routes = Blueprint('student_routes', __name__)

def get_db():
    conn = sqlite3.connect('school.db')
    conn.row_factory = sqlite3.Row
    return conn

@student_routes.route('/students', methods=['GET'])
def get_students():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return jsonify([dict(student) for student in students]), 200

@student_routes.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data or 'roll_number' not in data or 'grade' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, roll_number, grade) VALUES (?, ?, ?)",
            (data['name'], data['roll_number'], data['grade'])
        )
        conn.commit()
        return jsonify({"message": "Student added successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Roll number must be unique"}), 400
    finally:
        conn.close()