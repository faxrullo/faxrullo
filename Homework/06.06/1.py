import os
os.system("cls")
ls=list(map(int,input("List elementlarini kiritting: ").split()))
y=lambda x:x*x
for x in range(len(ls)):
    ls[x]=y(ls[x])
print(ls)