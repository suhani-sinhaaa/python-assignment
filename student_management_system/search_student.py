def search():
    try:
        id_to_search = input("Enter student's ID to search: ")
        with open('students.txt', 'r') as f:
            students = f.readlines()
            flag = False

            for student in students:
                name, id = student.strip().split('-')
                if id == id_to_search:
                    print("\nStudent Found:\n")
                    print(f"Name: {name}, ID: {id}")
                    flag = True
                    break
            if not flag:
                print("Student not found")
    except Exception as e:
        print("An error occurred while searching for a student")
