import os
os.system("cls")
os.chdir("C:\\file example")
def tub(son):
    for x in range(2,int(son**(1/2))+1):
        if son%x==0:
            return False
    return True
n=int(input("n ni qiymatini kiriting: "))
f=open("2-masala.txt","w+")
for x in range(2,n):
    if tub(x):
        f.write(str(x)+" ")
print("Faylga ma'lumot yozildi")
