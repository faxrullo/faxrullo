import os
os.system("cls")
son1,son2=map(int,input("Sonlarni kiriting: ").split())
a=son1
b=son2
while son1==son2:
    if son1>son2:
        son1-=son2
    else:
        son2-=son1
print(f"EKUB{a,b}={son1}")