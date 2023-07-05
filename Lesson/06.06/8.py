import os
os.system("cls")
ls=[('item1','12.20'),('item2','15.10'),('item3','24.50')]
result=sorted(ls,key=lambda x: x[1])
print(result)