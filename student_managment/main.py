students = []

def show_menu():
    print("\n--- Student Management System ---")
    print("1. Add student")
    print("2. View students")
    print("3. Delete student")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students.append({"name": name, "grade": grade})
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"Name: {student['name']}, Grade: {student['grade']}")

    elif choice == "3":
        name_to_delete = input("Enter student name to delete: ")

        found = False
        for student in students:
            if student["name"].lower() == name_to_delete.lower():
                students.remove(student)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")