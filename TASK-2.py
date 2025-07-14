import csv
csv=open("C:/Users/user/Desktop/STUDENT.csv","r")

def read_students_csv():
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            top_score = 0
            top_student = ""
            for row in reader:
                try:
                    marks = [int(row['math']), int(row['science']), int(row['english'])]
                    total = sum(marks)
                    average = total / len(marks)
                    print(f"{row['name']} - Total: {total}, Average: {average:.2f}")
                    if total > top_score:
                        top_score = total
                        top_student = row['name']
                except Exception as e:
                    print(f"Error in data: {row}, Error: {e}")
            print(f"Top Scorer: {top_student} with {top_score} marks")
    except FileNotFoundError:
        print("CSV file not found.")

# Example usage:
# read_students_csv('students.csv')
