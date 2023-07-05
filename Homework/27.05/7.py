import os
os.system("cls")
son=int(input("Sonni kiriting: "))
f1=1
f2=1
for x in range(1,son):
    f=f1+f2
    f1=f2
    f2=f
    if f>son:
        print(f"Result: {f}")
        break