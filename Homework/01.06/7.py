import os
os.system("cls")
sana=map(str,input("Sanani kiriting: ").split("."))
sana=list(sana)
kun=int(sana[0])
oy=int(sana[1])
yil=int(sana[2])
kun+=7
if kun>31:
    match oy:
        case 1,3,5,7,8,10,12: 
            oy+=1
            kun-=31
            if oy>12:
                yil+=1
elif kun>30:
    match oy:
        case 4,6,9,11: 
            oy+=1
            kun-=31
            if oy>12:
                yil+=1
elif kun>28: 
        oy+=1
        kun-=31
        if oy>12:
            yil+=1     
sana[0]=kun
sana[1]=oy
sana[2]=yil
print(sana)
