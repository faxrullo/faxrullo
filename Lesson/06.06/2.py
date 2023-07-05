import os
os.system("cls")

def erase(ls):
    ls1=[]
    for x in ls:
        if ls.count(x)>1 and x not in ls1:
            ls1.append(x)
    for x in ls:
        if x in ls1:
            ls.remove(x)
    return len(ls1)
print(erase(list(map(int,input("List elementlarini kiriting: ").split()))))
        
