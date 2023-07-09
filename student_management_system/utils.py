def initialize():
    try:
        with open('students.txt', 'w') as f:
            pass
    except Exception as e:
        print("An error occurred while initializing the student database")
