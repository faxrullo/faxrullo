import os
os.system("cls")
n=int(input("List elementlari sonini kiriting: "))
ls=[]
tp=tuple()
for x in range(n):
    tp=input("Familiya va ismni kiriting: ")
    ls.append(tp)
familya=sorted(ls,key=lambda x: x[0])
ism=sorted(ls,key=lambda x: x[1])
print(familya)
print(ism)