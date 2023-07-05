import os
os.system("cls")
son=input("Sonni kiriting: ")
son=int(son)
son=(son%10)*100+son//10
print(f"Result: {son}")