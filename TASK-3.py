import csv
csv=open("C:/Users/user/Desktop/STUDENT.csv","r")

def append_student_data("C:/Users/user/Desktop/STUDENT.csv","r"):
    name = input("Enter student name: ")
    marks = []
    for subject in ['Math', 'Science', 'English']:
        mark = input(f"Enter marks for {subject}: ")
        marks.append(mark)

    with open(filename, 'a', newline='') as file:
        writer = csv.writer("C:/Users/user/Desktop/STUDENT.csv","r")
        writer.writerow([name] + marks)
        print("Student data added successfully.")

# Example usage:
# append_student_data('students.csv')
