import os
os.system("cls")
ls1=list(map(str,input("1-list ma'lumotlarini kiriting: ").split()))
ls2=list(map(str,input("2-list ma'lumotlarini kiriting: ").split()))
ls3=list(map(str,input("3-list ma'lumotlarini kiriting: ").split()))

dc2=dict.fromkeys(ls1,None)
for x,y,z in zip(ls2,ls3,ls1):
    dc2[z]=dict.fromkeys(x,y)
print(dc2)
