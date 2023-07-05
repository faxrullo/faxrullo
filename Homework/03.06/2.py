import os
os.system("cls")
st=input("Satrni kiriting: ")
dc=dict()
st=list(st)
for x in st:
    dc[x]=st.count(x)
print(dc)