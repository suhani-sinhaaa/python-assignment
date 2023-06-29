# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures

def ds(roll_no,name):
    my_list=[roll_no,name]
    my_tuple=(roll_no,name)
    my_set={roll_no,name}
    my_dictionary={"roll_no":roll_no,"name":name}

    
    print("Initial Data Structures Values:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dictionary)

    my_list[0]=99
    my_tuple="14","Esha"
    my_set.remove(roll_no)
    my_set.add(27)
    my_dictionary["name"]="suhani"

    print("Data Structures Values After Changes:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dictionary)

    del my_list
    del my_tuple
    del my_set
    del my_dictionary
    print("Data structures deleted")

ds(18,'pari')

    

    
    
    

