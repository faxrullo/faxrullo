import os
os.system("cls")
for x in range(100,1000):
    if(x//100==(x//10)%10 or x//100==x%10 or x%10==(x//10)%10):
        print(x,end=" ")