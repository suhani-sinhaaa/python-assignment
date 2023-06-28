ls = []
for i in range(5):
    num = int(input(f"enter number  {i+1}= "))
    ls.append(num)
   
    #Sum
print("The sum=",sum(ls))
    #smallest number
print("The smallest number=",min(ls))
    #largest number
print("The largest numeber=",max(ls))
    #Ascending order
ls.sort()
print("Ascending order=",ls)
    #Descending order
ls.sort(reverse=True)
print("Descending order=",ls)


    #list to tuple
print(f"list to tuple: {tuple(ls)}")


    #delete the list
del ls
print("list is deleted")

