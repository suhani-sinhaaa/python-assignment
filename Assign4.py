#break=>The loop exits
a="suhani"
for i in a:
    if(i=="h"):
        break
    else:
        print(i)

#Continue=>skips the  current iteration and moves to the next one
a="suhani"
for i in a:
    if(i=="h"):
        continue
    else:
        print(i)

#pass=>used as a null statement,so that no error arises and code executes
a="suhani"
for i in a:
    if(i=="h"):
        pass
    else:
        print(i)

#for with else
a="suhani"
for i in a:
    if(i=="h"):
        continue
    else:
        print(i)
else:
    print("There is a continue statement")

#while with else
i=1
while(i<=10):
    if(i==5):
        i+=1
        continue
    else:
        print(i)
        i+=1
else:
    print("It has continue")       
