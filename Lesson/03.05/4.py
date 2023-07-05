import os
os.system("cls")
dc=dict()
ls=input("Satrni kiriting: ")
ls1=list(map(str,input("So'zlarni kiriting: ").split()))
ls=ls.split()
dc=dc.fromkeys(ls1,0)
for y in ls1:
    dc[y]=ls.count(y)
print(dc)

