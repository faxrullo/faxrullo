import os
os.system("cls")
os.chdir("C:\\faxrillo")
filename=input("Fayl nomini kiriting: ")
f=open(filename,"r")
soz=f.read()
ls=soz.split(" ")
print(ls[0] ls[-1]) 
f.close()