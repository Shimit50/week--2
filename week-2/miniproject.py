@student_routes.route('/students/search', methods=['GET'])
def search_students():
    name = request.args.get('name')
    grade = request.args.get('grade')
    if not name and not grade:
        return jsonify({"error": "Provide name or grade"}), 400

    conn = get_db()
    cursor = conn.cursor()
    if name and grade:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ? AND grade = ?",
            (f"%{name}%", grade)
        )
    elif name:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            (f"%{name}%",)
        )
    else:
        cursor.execute(
            "SELECT * FROM students WHERE grade = ?",
            (grade,)
        )
    students = cursor.fetchall()
    conn.close()
    return jsonify([dict(student) for student in students]), 200