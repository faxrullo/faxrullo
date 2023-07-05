import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
S=0
print("S",end="=")
for x in range(1,n+1):
    S+=1/n
    print(f"1/{x}",end="")
    if x!=n:
        print(end="+")
print(f"\nResult: {S}")
