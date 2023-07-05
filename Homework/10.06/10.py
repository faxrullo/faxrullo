import os
os.system("cls")
os.chdir("C:\\faxrillo")
f=open("Full_name.txt","r")
ls=[]
for x in ls:
    ls[x]=    temp=[]
    st=f.readline()
    temp=st.split()
    ls.append(temp)
sorted(ls,key=lambda x: x[1])
print(ls)