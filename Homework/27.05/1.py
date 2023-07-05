import os
os.system("cls")
age=int(input("Yoshizni kiriting: "))
for x in range(1,200):
    if x==age:
        print(f"Yizning yoshingiz: {x}",end="  ")
    print(x,end=" ")