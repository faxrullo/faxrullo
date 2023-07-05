import os
os.system("cls")
os.chdir("C:\\file example")
f=open("6-masala.txt","w+")
satr=input("Satrni kiriting: ")
f.write(satr)
f.seek(0)
st=f.read()
ls=st.split()
for x in ls:
    if x[-1] not in ('.',',','?','!'):
        if len(x)>3:
            print(x)
    else:
        x=x[:len(x)-1]
        if len(x)>3:
            print(x)