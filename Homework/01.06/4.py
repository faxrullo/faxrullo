import os
os.system("cls")
son=int(input("Sonni kiriting: "))
ls=[]
for x in range(2,son):
    a=False
    for y in range(2,int(x**(1/2))):
        if x%y==0:
            a=True
            break
    if a==False:
        ls.append(x)
ls1=[]
for x in ls:
    while son!=1:
        if son%x==0:
            son/=x
            ls1.append(x)
        else: 
            break
print(ls1)