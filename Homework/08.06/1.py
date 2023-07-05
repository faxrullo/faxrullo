import os
os.system("CLS")
ls=os.listdir()
sch=[0,0,0]
key=['.doc','.txt','.other']
for x in ls:
    if ".doc" in x:
        sch[0]+=1
    elif ".txt" in x:
        sch[1]+=1
    else:
        sch[2]+=1
dc=dict()
dc.fromkeys(key,None)
for x,y in zip(key,sch):
    dc[x]=y
print(dc)