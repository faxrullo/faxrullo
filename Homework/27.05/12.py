import os
os.system("cls")
son=int(input("Sonni kiriting: "))
sum=0
while son:
    if (son%10)%2:
        sum+=son%10
    son//=10
print(f"Result: {sum}")