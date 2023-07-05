import os
os.system("cls")
son=input("Sonni kiriting: ")
son=int(son)
son=(son%10)*100+((son//10)%10)*10+son//100
print(f"Natija: {son}")