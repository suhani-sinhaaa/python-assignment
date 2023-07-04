import Assign9 as a
obj=a.math_operations()
while True:
    print("MENU DRIVEN:")
    print("Press 1 if you want to perform numeric operations")
    print("Press 2 if you want to perform Aritmetic operations")
    print("Press 3 if you want to perform Trignometric operations")    
    print("Press 4 if you want to perform Set operations")
    print("Press 5 if you want to perform Logarithmic operations")
    S=int(input("Enter your choice"))
    if(S==1):
        obj.math_functions(25,5)
        s=int(input("If you want to exit press 1 or else press 0"))
    elif(S==2):
        obj.Arithmetic(40,10)
        s=int(input("If you want to exit press 1 or else press 0"))
    elif(S==3):
        obj.Trigonometry(2)
        s=int(input("If you want to exit press 1 or else press 0"))
    elif(S==4):
        a=[1,2,3,4,5]
        b=[1,2,4,6,7]
        obj.Set_operations(0,0)
        s=int(input("If you want to exit press 1 or else press 0"))
    elif(S==5):
        obj.Log_op(10)
        s=int(input("If you want to exit press 1 or else press 0"))
    else:
        print("Invalid Choice")
    if s==1:
        exit()
    

        


    