import os
os.system("cls")
os.chdir("C:\\faxrillo")
ls=list(map(str,input("Yaratiladigan fayl nomlarini kiriting: ").split()))
count=0
for x in ls:
    try: 
        f=open(x,"x")
    except:
        continue
    else:
        count+=1
print(f"{count} ta yangi fayl yaratildi")
