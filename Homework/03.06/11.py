import os
os.system("cls")
ls1=list(map(int,input("Dictionary keyslarini kiriting: ").split()))
ls2=list(map(int,input("Dictionart valuelarini kiriting: ").split()))
dc={}
for x,y in zip(ls1,ls2):
    dc[x]=y
ls1.sort(reverse=True)
sch=0
for x in ls1:
    if sch==3: 
        break
    print(x,end=" ")
    sch+=1