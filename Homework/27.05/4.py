import os
os.system("cls")
for x in range(10,100):
    for y in range (2,int(x**(1/2))+1):
        if x%y==0:
            break
        elif y==int(x**(1/2)):
            print(x,end=" ")