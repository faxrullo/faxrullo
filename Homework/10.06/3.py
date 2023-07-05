import os
os.system("cls")
os.chdir("C:\\file example")
f=open("3-masala.txt",'w+')
sonlar=input("Sonalrni kiriting: ")
f.write(sonlar)
f.seek(0)
st=f.read()
ls=st.split()
sum=0
for x in ls:
    sum+=float(x)
print(sum)