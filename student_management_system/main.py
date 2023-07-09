from add_student import add
from delete_student import delete
from search_student import search
from update_student import update
from view_students import view

def main_menu():
    while True:
        print("Welcome to the Student Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. View Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            delete()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            view()
        elif choice == '6':
            print("Thank you for using the Student Management System")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
