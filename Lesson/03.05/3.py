import os
os.system("cls")
dc={"Alisher":28,"Jamila":24,"Komila":18,"Aziza":32}
Max=0
a=0
for x in dc:
    if Max < dc[x]:
        Max=dc[x]
print(Max)