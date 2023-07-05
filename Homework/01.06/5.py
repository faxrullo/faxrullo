import os
os.system("cls")
ls=list(map(int,input("List elementlarini kiriting: ").split()))
ls1=ls.copy()
ls2=[]
for x in range(len(ls)):
    for j in range(x,len(ls)-1):
        ls[j],ls[j+1]=ls[j+1],ls[j]
        ls2.append(ls)
        ls=ls1.copy()
print(ls2)

