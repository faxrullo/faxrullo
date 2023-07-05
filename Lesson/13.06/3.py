import os
os.system("cls")
os.chdir("C:\\faxrillo")
def check_number(res):
    res=res.split()
    temp=res[2]+res[3]+res[4]
    ln=len(temp)
    res=set()
    for x in temp:
        res.add(int(x))
    if len(res)==ln:
        return True
    else: 
        return False
f=open("number.txt","r")
number=f.read()
number=number.split('\n')
keys=[]
dc=dict()
for x in number:
    if check_number(x):
        print(x)
for x in number:
    res=x.split()
    keys.append(res[1])
dc.fromkeys(keys,0)
for x in keys:
    dc[x]=keys.count(x)
print(dc)