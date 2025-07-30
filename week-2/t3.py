@student_routes.route('/students/<roll_number>', methods=['PUT'])
def update_student(roll_number):
    data = request.get_json()
    if not data or 'grade' not in data:
        return jsonify({"error": "Grade is required"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET grade = ? WHERE roll_number = ?",
        (data['grade'], roll_number)
    )
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated successfully"}), 200

@student_routes.route('/students/<roll_number>', methods=['DELETE'])
def delete_student(roll_number):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll_number,))
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted successfully"}), 200