import os
os.system("cls")
data=input("Sana va vaqtni kiriting: ")
ls=[] 
st=""
for x in data:
    if x!=" " and x!=':' and x!=".":
        st+=x
    else:
        ls.append(st)
        st=""
ls.append(st)
day=""
ls[0]=int(ls[0])
ls[0]=str(ls[0])
match int(ls[1]):
    case 1:
        day=ls[0]+" January "
    case 2:
        day=ls[0]+" February "
    case 3:
        day=ls[0]+" March "
    case 4:
        day=ls[0]+" April "
    case 5:
        day=ls[0]+" May "
    case 6:
        day=ls[0]+" June "
    case 7:
        day=ls[0]+" July "
    case 8:
        day=ls[0]+" August "
    case 9:
        day=ls[0]+" September "
    case 10:
        day=ls[0]+" Octomber "
    case 11:
        day=ls[0]+" November "
    case 12:
        day=ls[0]+" December "
ls[3],ls[4]=int(ls[3]),int(ls[4])
ls[3],ls[4]=str(ls[3]),str(ls[4])
day+=ls[2]+" year "+ls[3]+" hours "+ls[4]+" minutes"
print(day)