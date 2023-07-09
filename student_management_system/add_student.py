def add():
    try:
        with open('students.txt', 'a') as f:
            name = input("Enter student's name: ")
            id = input("Enter student's ID: ")
            
            f.write(f"{name}-{id}\n")
            print("Successfully added a student")
    except Exception as e:
        print("An error occurred while adding a student")
