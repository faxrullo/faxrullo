import os
os.system("cls")
ls=[('item1','12.20'),('item2','15.10'),('itme3','24.5')]
for x in range(len(ls)-1):
    ls[0]=list(ls[0])
    for y in range(x+1,len(ls)):
       ls[y]=list(ls[y])
       if ls[x][1]<ls[y][1]:
           ls[x],ls[y]=ls[y],ls[x]
for x in range(len(ls)):
        ls[x]=tuple(ls[x])  
print(ls)