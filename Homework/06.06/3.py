import os
os.system("cls")
ls=[]
for x in range(20):
    ls.append((x+10)*(3**x)%100)
print(ls)
juft=list(filter(lambda x: x%2==0,ls))
toq=list(filter(lambda x: x%2==1,ls))
print(f"Listning juft elementlari: {juft}")
print(f"Listning toq elementlari: {toq}")