import os
os.system("cls")
ls=[(),(),('d'),('a','b','c',),('d')]
for x in range(len(ls)):
    ls[x]=list(ls[x])
    if ls[x]=="":
        ls.pop(x)
print(ls)