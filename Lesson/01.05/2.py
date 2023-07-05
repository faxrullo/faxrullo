import os
os.system("cls")
a,b=map(int,input("A va B ni kiriring: ").split())
res=[a]
count=0
a=a/2 
while a>b:
    res.append(a)
    count+=1
    a=a/2
print(count)
print(res)