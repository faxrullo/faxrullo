import os
os.system("cls")
son =int(input("Sonni kiriting: "))
son=str(son)
ln=len(son)
son=int(son)
s=""
while 1:
    s+=str((son%(10**ln))//(10**(ln-1))*(10**(ln-1)))
    s+='+'
    ln-=1      
    if ln==0:
        break 
s=s[:len(s)-1]
print(s)
    