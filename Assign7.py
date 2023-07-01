def fileHandling(file):
    print("File handling")
    file_s = open(file, "a+")
    print("File opened successfully")
    try:
        name = input("Enter your name: ")
        Roll_no = int(input("Enter your roll number: "))
        class_name = input("Enter your class name: ")
        file_s.writelines(name)
        file_s.writelines(str(Roll_no)) 
        file_s.writelines(class_name + "\n")  
    except IOError:
        print("IO exception is handled")
    except Exception:
        print("The exception is handled")
    except FileExistsError:
        print("The exception is handled")
    except FileNotFoundError:
        print("The exception is handled")
    finally:
        print("No more exceptions")
        file_s.close()  
    file_s = open(file, "r")  
    file_content = file_s.readlines()
    print("file_content:")
    print(file_content)
    print("The content is read successfully")
    file_s.close()
    print("File closed")

fileHandling("source.txt")
