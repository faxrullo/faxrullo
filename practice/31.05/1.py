import os
os.system("cls")
ls=[10,1,2,3,4,5]
tp=[6,7,8,9]
ls.extend(tp)
ls.sort()
ln=len(ls)+len(tp
print(ln-4)
print(ls)
if ln%2:
    print(ls[ln//2])
else:
    n=ls[(ln//2)-1]+ls[ln//2]
    print(n/2)
    ls[0]=list(ls[0])
    ls[0]=tuple(ls[0])