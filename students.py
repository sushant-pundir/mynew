students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")