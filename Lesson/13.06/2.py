import os
import pickle
os.system("cls") 
os.chdir("C:\\file example")
f=open("palyer.dat","rb+")
while True:
    res=pickle.load(f)
    if res==None:
        break
    print(f"Name:  { res[0]}")
    print(f"Age:   { res[1]}")
    print(f"Club:  { res[2]}")
    print(f"Salary:{ res[3]}")
    print("*"*25)
    if f.res[1] > 30:
        f.res[3] -= 5000
    else:
        f.res[3]+=5000
    print(f"Name:  { res[0]}")
    print(f"Age:   { res[1]}")
    print(f"Club:  { res[2]}")
    print(f"Salary:{ res[3]}")
    print("-"*25)
f.close()