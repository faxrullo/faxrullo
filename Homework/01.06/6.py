import os
os.system("cls")
ls=list(map(int,input("List elementlarini kiriting: ").split()))
res=[]
temp=[]
a=None
for x in range(len(ls)-1):
    a=False
    if ls[x]<ls[x+1]:
        res.append(ls[x])
        a=True
    elif len(res)>0:
        res.append(ls[x])
        temp.append(res)
        res=[]
if a:
    res.append(ls[x+1])
    temp.append(res)
print(temp)