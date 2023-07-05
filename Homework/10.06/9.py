import os
os.system("cls")
os.chdir("C:\\faxrillo")
f=open("internet.txt","r")
ls=f.readlines()  
key=[]
for x in range(len(ls)):
    ls[x]=ls[x].split(',')
    ls[x][3].remove('/n')
    key.append(ls[x][3])
    ls[x][2]=ls[x][2].split("-")
    check1=0
    check2=0
    '''for y in ls[x][2]:
        if y.isalpha():
            check1+=1
        elif y.isdigit():
            check2+=1
    if check1==6 and check2==6:
        print(f"Email: {ls[x][0]}, File_name: {ls[x][3]}")
    else:
        break'''
dc=dict()
dc.fromkeys(key)
for x in key:
    dc[x]=key.count(x)
    while x in key:
        key.remove(x)
print(dc)
