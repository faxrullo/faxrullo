import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
check=True
sum=0
for x in range(2,n,1):
    for y in range(2,x,1):
        sum=0
        while x>=sum:
            sum+=y
            if sum==x:
                check=False
        if check==False:
            break
    if check==True:
        print(x,end=" ")
    else:
        check=True