import os
os.system("cls")
dc={1:10,2:20,3:30,4:40,5:50,6:60}
ls=list(dc)
ls.sort()
dc1={}
ls.remove(max(ls))
ls.remove(min(ls))
for x in ls:
    dc1[x]=dc[x]
print(dc1)