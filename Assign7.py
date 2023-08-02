class File:
    def fileHandling(cls, file="src.txt"):
        try:
            with open(file, "a+") as z:
                z.writelines(["name:Suhani\n", "Rollno:14\n", "class:TYIF"])
                z.seek(0)
                print(z.readlines())
        except FileNotFoundError:
            print("File not found.")
        except FileExistsError:
            print("File already exists.")
        except IOError:
            print("Input/Output error occurred.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("This is the finally block")

File.fileHandling("src.txt")
