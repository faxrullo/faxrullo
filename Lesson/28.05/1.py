import os
os.system("cls")
a,b,c=map(float,input("Sonlarni kriting: ").split())
max=a
if max<b:
    max=b
if max<c:
    max=c
print("Natija: {}".format(max))
