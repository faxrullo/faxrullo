import os
os.system("cls")
ls=list(map(int,input("Sonalrni kiritingz: ").split()))

while 1:
    check=True
    for x in ls:
        if ls.count(x)<2:
            ls.remove(x)
            check=False
    if check==True:
        break
print(ls)