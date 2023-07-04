import math

class divisionby5(Exception):
    def __init__(self, message):
        super().__init__(message)

class math_operations:
    def math_functions(self, a):
        print("The Floor value:", math.floor(a))
        print("The ceil value:", math.ceil(a))
        print("The square root:", math.sqrt(a))
        print("The absolute value", math.fabs(a))
        print("The factorial is:", math.factorial(a))

        # Reverse of a number
        rev = 0
        temp = a
        while temp > 0:
            last = temp % 10
            rev = (rev * 10) + last
            temp //= 10
        print("The reverse of a number is:", rev)

    def Arithmetic(self, a, b):
        print("Addition of a and b:", a + b)
        print("Subtraction of a and b:", a - b)
        print("Multiplication of a and b:", a * b)

        try:
            if b == 0:
                raise ZeroDivisionError("Division by zero error")
            print("Division of a and b:", a / b)
            print("Modulus of a and b:", a % b)
        except ZeroDivisionError as zde:
            print(zde)

        try:
            if b == 5:
                raise divisionby5("Cannot divide a number by 5")
        except divisionby5 as db:
            print(db)

        print("Exponential of a and b:", a ** b)

    def Trigonometry(self, a):
        print("The sin value:", math.sin(a))
        print("The cos value:", math.cos(a))
        print("The tan value:", math.tan(a))

    def Set_operations(self, a, b):
        set_union = set(a).union(set(b))
        print("Union=", set_union)
        set_intersection = set(a).intersection(set(b))
        print("Intersection=", set_intersection)
        set_difference = set(a).difference(set(b))
        print("Difference=", set_difference)
        set_symmetric_diff = set(a).symmetric_difference(set(b))
        print("Symmetric Difference=", set_symmetric_diff)

    def Log_op(self, x):
        log_10 = math.log10(x)
        print(f"Log base 10 of {x}: {log_10}")
        log_e = math.log(x)
        print(f"Natural logarithm of {x}: {log_e}")


obj = math_operations()

while True:
    print("MENU DRIVEN:")
    print("Press 1 if you want to perform numeric operations")
    print("Press 2 if you want to perform Arithmetic operations")
    print("Press 3 if you want to perform Trigonometric operations")
    print("Press 4 if you want to perform Set operations")
    print("Press 5 if you want to perform Logarithmic operations")
    
    S = int(input("Enter your choice: "))

    if S == 1:
        obj.math_functions(25)
        s = int(input("If you want to exit press 1 or else press 0: "))
    elif S == 2:
        obj.Arithmetic(40, 10)
        s = int(input("If you want to exit press 1 or else press 0: "))
    elif S == 3:
        obj.Trigonometry(2)
        s = int(input("If you want to exit press 1 or else press 0: "))
    elif S == 4:
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 4, 6, 7]
        obj.Set_operations(a, b)
        s = int(input("If you want to exit press 1 or else press 0: "))
    elif S == 5:
        obj.Log_op(10)
        s = int(input("If you want to exit press 1 or else press 0: "))
    else:
        print("Invalid Choice")
        s = int(input("If you want to exit press 1 or else press 0: "))

    if s == 1:
        exit()
