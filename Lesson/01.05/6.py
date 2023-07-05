import os
os.system("cls")
ls1=list(map(str,input("1-listga ma'lumotlarni to'ldiring: ").split()))
ls2=list(map(str,input("2-listga ma'lumotlarni to'ldiring: ").split()))
res=[]
i=3
j=3
for x,y in zip(ls1,ls2):
    if x+y=="shareshare":
        i+=2
        j+=2
    elif x+y=="sharesteal":
        i-=1
        j+=3
    elif x+y=="stealshare":
        i+=3
        j-=1
res=i+j
print(res)