# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures

def ds(roll_no,name):
    ls=[]
    ls.append((roll_no,name))
    t=(roll_no,name)
    s=set()
    s={(roll_no,name)}
    d={"roll_no":roll_no,"name":name}

    
    print("Initial Data Structures Values:")
    print("List:", ls)
    print("Tuple:", t)
    print("Set:", s)
    print("Dictionary:",d)

    ls[0]=(14,"esha")
    t=(18,"muskan")
    s.pop()
    s.add((51, "sara"))
    d["name"]="suhani"
    d["roll_no"]=51

    print("Data Structures Values After Changes:")
    print("List:", ls)
    print("Tuple:", t)
    print("Set:", s)
    print("Dictionary:",d)

    del ls
    del t
    del s
    del d
    print("Data structures deleted")

ds(18,'pari')

    

    
    
    

