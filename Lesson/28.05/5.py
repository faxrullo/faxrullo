import os
os.system("cls")
str=input("Satrni kiriting: ")
for x in str:
    sch=0
    for y in str:
        if x==y:
            sch+=1
    print(f"'{x}' -{sch} marta")

        
        