import os
os.system("cls")
son=input("Sonni kiriting: ")
son=int(son)
sum=son%10+(son//10)%10+son//100
print(f"Natija: {sum}")