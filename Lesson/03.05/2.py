import os
os.system("cls")
st=set(map(str,input("Set elementlarini kiriting: ")))
s=input("Qidirilayotgan qiymatni kiriting: ")
a=False
for x in st:
    a=False
    if x==s:
        print("Mavjud")
        a=True
        break
if a==False:
    print("Mavjud emas")