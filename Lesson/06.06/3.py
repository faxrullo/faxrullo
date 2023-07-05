import os
os.system("cls")

def sum_list(ls):
    a=True
    for x in range(len(ls)):
        if ls[x]<0 and a:
            manfiy=ls[x]
            a=False
        if ls[x]>0:
            musbat=ls[x]
    if manfiy != None and musbat!=None:
        sum=0
        for x in range(ls.index(manfiy)+1,ls.index(musbat)):
            sum+=ls[x]
        return sum
    else:
        return -1
    
print(sum_list(list(map(int,input("List elementlarini kiriting: ").split()))))