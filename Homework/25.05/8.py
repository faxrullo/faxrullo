import os
os.system("cls")
son=input("Sonni kiriting: ")
son=int(son)
print("Birlar xonasi: {0}\nO'nlar xonasi: {1}".format(son%10,(son//10)%10))