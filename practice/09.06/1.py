import os
os.system("cls")
os.chdir()
ls=os.listdir()
count=0
for x in ls:
    if ".docx" in x:
        count+=1
print(count)
