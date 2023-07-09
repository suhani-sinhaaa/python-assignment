def delete():
    try:
        id_to_delete = input("Enter student's ID to delete: ")
        with open('students.txt', 'r') as f:
            students = f.readlines()
        with open('students.txt', 'w') as f:
            flag = False
            for student in students:
                name, id = student.strip().split('-')
                if id != id_to_delete:
                    f.write(student)
                else:
                    flag = True
            
            if flag:
                print('Successfully deleted the student')
            else:
                print('Student not found')
    except Exception as e:
        print('An error occurred while deleting a student')
