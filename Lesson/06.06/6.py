import os
os.system("cls")
def tub(x):
    a=True
    for y in range(2,int(x**(1/2)+1)):
        a=True
        if x%y==0:
            a=False
            break
    if a:
        return x
list1=[3,15,17,25,19]    
print(list(filter(lambda x: (tub(x)),list1)))
