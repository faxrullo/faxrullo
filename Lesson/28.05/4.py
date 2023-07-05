import os
os.system("cls")
str=input("Satrni kiriting: ")
count=0
for x in str:
    if(x=='o'or x=='a' or x=='i' or x=='e'or x=='u'or x=='O'or x=='A' or x=='I' or x=='E'or x=='U'):
        count+=1
print(f"Berilgan satrdagi unli harflar soni {count} ta")