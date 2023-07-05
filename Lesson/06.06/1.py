import os
os.system("cls")

def calculator(x,amal,y):
    if amal=='+':
        print(x+y)
    elif amal=='-':
        print(x+y)
    elif amal=='*':
        print(x*y)
    elif amal=='/':
        print(x/y)
    elif amal=='%':
        print(x%y)
    else: 
        print(f"siz noto'g'ti amal {amal} kiritidingiz")
    
x,amal,y=map(str,input("Ifodani kiriting: ").split())
x,y=int(x),int(y)
calculator(x,amal,y) 