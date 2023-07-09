def update():
    try:
        id_to_modify = input("Enter student's ID to modify: ")
        with open('students.txt', '+r') as f:
            students = f.readlines()
            flag = False

            for i, student in enumerate(students):
                name, id = student.strip().split('-')
                if id == id_to_modify:
                    flag = True

                    print("\nCurrent Student Details:\n")
                    print(f"Name: {name}, ID: {id}")

                    new_name = input("Enter student's new name: ")
                    new_id = input("Enter student's new ID: ")

                    if new_name:
                        students[i] = f"{new_name}-{new_id}\n"
                    else:
                        students[i] = f"{name}-{id}\n"
                    
                    f.seek(0)
                    f.writelines(students)
                    f.truncate()

                    print("Successfully updated student's details")
                    break

            if not flag:
                print("Student not found")
    except Exception as e:
        print("An error occurred while updating a student")
