import os
os.system("cls")
x=int(input("Sonni kiriting: "))
count=0
while x:
    if x%7==0:
        print(x,end=" ")
        count+=1
    x-=1
print("Reslut: ",count)