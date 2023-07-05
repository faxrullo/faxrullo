import os
os.system("cls")
son=int(input("sonni kiriting: "))
check=True
for x in range(2,int(son**(1/2))):
    if son%2:
        continue
    else:
        check=False
        break
if check==True:
    print(f"{son} - Tub son")
else:
    print(f"{son} - Tub emas")