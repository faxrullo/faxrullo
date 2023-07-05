import os
os.system("cls")
ls=list(map(int,input("List elmenetlarini kiriting: ").split()))

for x in range(len(ls)-1):
    for y in range(x+1,len(ls)):
        if str(ls[x])<str(ls[y]):
            ls[x],ls[y]=ls[y],ls[x]
sum=0
for x in range(len(ls)-1):
    sum=(sum+ls[x])*(10**len(str(ls[x+1])))
sum+=ls[len(ls)-1]
print(f"Reslut: {sum}")