import os
os.system("cls")
def nearest_value(st,n):
    Min=n**n
    son=0
    for x in st:
        if abs(x-n)<Min:
            Min=abs(x-n)
            son=x
    return son
s=set(map(int,input("Set elementlarini kirting: ").split()))
n=int(input("N="))
print(nearest_value(s,n))