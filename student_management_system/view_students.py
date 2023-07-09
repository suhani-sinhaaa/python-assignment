def view():
    try:
        with open("students.txt", 'r') as f:
            students = f.readlines()
            if students:
                print("\nStudents:\n")
                for student in students:
                    name, id = student.strip().split('-')
                    print(f"Name: {name}, ID: {id}")
            else:
                print("The student database is empty")
    except Exception as e:
        print("An error occurred while viewing students")
