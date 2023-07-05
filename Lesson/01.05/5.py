import os
os.system("cls")
temp=[  ]
k=[]
n=int(input("n ni kiritng: "))
for x in range(n):
    k=list(map(int,input("sonlarni kirting: ").split()))
temp.append(k)
ls=list(list())
res=[]
for x in range(0,7):
    for y in range(x,7):
        res=x,y
        ls.append(res)
        res=[]
ls1=[]
for x in ls:
    if x not in temp:
        ls1.append(x)
print(ls1)
