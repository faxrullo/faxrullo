import os
os.system("cls")
ls=[(10,20,40),(40,50,60),(70,80,90)]
for x in range(len(ls)):
    tp=list(ls[x])
    tp[len(tp)-1]=100
    ls[x]=tuple(tp)
print(ls)