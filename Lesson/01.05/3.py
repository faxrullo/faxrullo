import os
os.system('cls')
ls=list(map(int,input("Elementlarni kiriting: ").split()))
res=[]
for x in ls:
    res.append(str(x))
ls=res.copy()
for x in range(len(ls)-1):
    for y in range(x+1,len(ls)):
        if len(ls[x])>len(ls[y]):
            ls[x],ls[y]=ls[y],ls[x]
ls=list(ls)
print(ls)