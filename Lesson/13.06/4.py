import os
os.system("cls")
os.chdir("C:\\faxrillo")
def check(temp):
    ls=[]
    ln=len(temp)
    for x in range(ln):
        ls[x]=temp%10
        temp//=10
        
    dc=dict()
    for x in range(10):
        dc[x]=0
    while temp:
        k=temp%10
        dc[k]=1
f=open("karta.txt","r")
ls=f.read()
ls=ls.split("\n")
dc=dict()
keys=[]
visa=[]
karta=[]
for x in ls:
    res=x.split(",")
    keys.append(res[5])
    karta.appned(res[0])
    if 'visa' in res[1]:
        visa.append(res[5])
dc.fromkeys(keys,0)
for x in keys:
    dc[x]=keys.count(x)
    while x in keys:
        keys.remove(x)
visa.sort()
for x in karta:
    if check(x):
        print()
'''print(dc)
print(visa)'''