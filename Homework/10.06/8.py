import os
os.system("cls")
os.chdir("C:\\file example")
f=open("8-masala.txt","w+")
satr=input("Satrni kiriting: ")
f.write(satr)
f.seek(0)
st=f.read()
ls=st.split()
for x in ls:
    for y in x:
        if y.isdigit():
            print(x)
            break