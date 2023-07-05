import os
os.system("cls")
a,b=map(int,input("A va B ni kiriting: ").split())
for x in range(a+1,b):
    n=0
    while x>n:
        print(x,end=" ")
        n+=1
    print()    