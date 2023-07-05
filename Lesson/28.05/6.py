import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
juft=""
toq=""
for x in range(1,n):
    if(x%2):
        x=str(x)
        toq=toq+x+' '
    else:
        x=str(x)
        juft=juft+x+' '
print("Juft sonlar: ",juft)
print("Toq sonlar: ",toq)