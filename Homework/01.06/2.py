import os
os.system("cls")
for x in range(1000,10000):
    ls=[]
    y=x
    while x:
        ls.append(x%10)
        x//=10
    if ls.count(ls[0])==1 and ls.count(ls[1])==1 and ls.count(ls[2])==1 and ls.count(ls[3])==1:
        print(y,end=" ")
