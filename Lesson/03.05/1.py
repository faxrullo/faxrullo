import os
os.system("cls")
ls=list(map(int,input("List elementlarinikiriting: ").split()))
ls1=set(ls)
print(len(ls)-len(ls1))