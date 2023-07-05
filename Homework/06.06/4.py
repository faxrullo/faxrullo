import os
os.system("cls")
st=input("Sonni kiriting: ")
count=0
for x in st:
    if int(x)==0:
        count+=1
    else:
        break
print(count)