import os
os.system("cls")
n=int(input("Sonni kiriting: "))
k=1
f=1
a=False
while n>=f:
    f*=k
    k+=1
    if n==f:
        a=True
ls=[]
for x in range(1,k-1):
    ls.append(x)
print(ls)