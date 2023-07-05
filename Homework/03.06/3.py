import os
os.system("cls")
ls1=list(map(str,input("Dictionary keyslarini kiriting: ").split()))
ls2=list(map(str,input("Dictionary valuelarini kiriting: ").split()))
dc1=dict.fromkeys(ls1,None)
ls=[]
for x,y in zip(ls1,ls2):
    dc1[x]=y
    ls.append(dc1[x])
print(dc1)
sch=0
for x in dc1:
    if sch<len(ls)-1:
        if (sch+1)%2:
            dc1[x]=ls[sch+1]
        elif (sch-1)%2==0:
            dc1[x]=ls[sch-1]
    sch+=1
print(dc1)


