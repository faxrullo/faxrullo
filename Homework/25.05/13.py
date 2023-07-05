import os
os.system("cls")
son=input("Sonni kiriting: ")
son=int(son)
son=((son%100)//10)*100+(son//100)*10+son%10
print(f"Natija: {son}")