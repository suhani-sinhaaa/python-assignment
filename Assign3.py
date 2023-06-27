n1=0
while(n1==0):
   print("Calculator Menu")
   print("1.Addition")
   print("2.Subtraction")
   print("3.Multiplication")
   print("4.Division")
   choice=int(input("Enter your choice\n"))
   n1=float(input("Enter the first number\n"))
   n2=float(input("Enter the second number\n"))
   if (choice==1):
      result=n1+n2
      print("Addition=",result)
      y=int(input("Enter 0 if you want to continue or press 1 to exit"))
   elif(choice==2):
      result=n1-n2
      print("Subtraction=",result)
      y=int(input("Enter 0 if you want to continue or press 1 to exit"))
      
   elif(choice==3):
      result=n1*n2
      print("Multiplication=",result)
      y=int(input("Enter 0 if you want to continue or press 1 to exit"))
      

   elif(choice==4):
       if(n2==0):
        print("Error: cannot divide a number by 0")
       else: 
        result=n1/n2
        print("Division=",result) 
        y=int(input("Enter 0 if you want to continue or press 1 to exit")) 
   else:
      print("Invalid choice")    

   if(y==1):
      exit()
   else:
      n1==y