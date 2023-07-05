import os
os.system("cls")
os.chdir("C:\\faxrillo")
f=open('Full_name.txt',"r")
F=open("Fist_name.txt","w")
full_name=f.readline() 
for x in ful_name:

ful_name=list(full_name.split())
Fist_name=sorted(full_name,key=lambda x: x[1])
F.writelines(Fist_name)
print(full_name[0][1])
#print(full_name)
f.close()
F.close()