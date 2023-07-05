import os
os.system("cls")
ls=[14,15,20,25]
ls1=[19,35,48,90]
ls2=[]
for x in range(len(ls1)):
    for y in range(len(ls)):
        if ls1[x]>ls[y]:
            ls.insert(y,ls1[x])
print(ls)