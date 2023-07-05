import os
import pickle
os.system("cls") 
os.chdir("C:\\file example")
f=open("palyer.dat","wb")
while True:
    temp=input("Faylga ma'lumot yozish uchun Yes ni tugatish No ni kiriting: ")
    if temp.lower()=="yes":
        name=input("Futbolchining ismini kiriting: ")
        age=int(input("Futbolchining yoshini kiriting: "))
        club=input("Futbolchining klubi: ")
        salary=int(input("Maoshini kiriting: "))
        pickle.dump([name,age,club,salary],f)
    else:
        break
f.close()