import os
os.system("cls")
st=input("Ma'lumotni kiriting: ")
st=st.split()
sch=0
for x in st:
    if x.isalpha():
        sch+=1
    else:
        if sch>=3:
            break
        else:
            sch=0
if sch>=3:
    print(True)
else:
    print(False)
