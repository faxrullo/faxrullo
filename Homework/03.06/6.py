import os
os.system("cls")
n=int(input("list elementlari sonini kiriting: "))
ls=list()
y=list()
ls1=[]
for x in range(n):
    y=list(map(str,input(f"{x+1} - list elementlarini kiriting: ").split()))
    ls.append(y)
    ls1.append(ls[x][0])
for x in range(n):
    if ls[x][0]==ls1[x]:
        ls[x].remove(ls1[x])
dc1=dict()
for x,y in zip(ls,ls1):
    dc1[y]=x
print(dc1)