import os
os.system("cls")
os.chdir("C:\\file example")
n=int(input("n ni qiymatini kiririting: "))
f=open("1-masala.txt","w+")
finish,satart,step=0,0,1
if n%2:
    finish=n+1
else:
    satart=n
    step=-1
for x in range(satart,finish,step):
    k=x
    sum=0
    while x:
        sum+=k
        if x!=1:
            f.write(str(k) + '+')
        else:
            f.write(str(k) + '=' + str(sum) + '\n')
        x-=1
print("faylga ma'lumot yozildi")
f.close()
    
    