import os
os.system("cls")
a,b,c=map(int,input("Sonlarni kiriting: ").split())
urta=(a+b+c)/3
count=0
if a>urta:
    count+=1
if b>urta:
    count+=1
if c>urta:
    count+=1
print("Natija: {}".format(count))