n=True
while(n==True):
    print("For addition press +")
    print("For subraction press -")
    print("For multiplication press *")
    print("For division press /")
    print("For floor division press //")
    print("For exponential press **")
    print("For modulus press %" )
    source=input("Enter the symbol for operation you want to perform")
    if source == "+":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a+b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "-":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a-b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "*":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a*b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "/":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a/b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "//":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a//b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "**":
        a=int(input("Enter the number"))
        n=int(input("Enter the raise to (^) number"))
        result=a**n
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif source == "%":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a%b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    if(j==1):
        exit()
    else:
        n=True