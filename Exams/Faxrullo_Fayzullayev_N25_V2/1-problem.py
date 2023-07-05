import os
os.system("cls")
bigger_price=[{"name":"bread","price":100},{"name":"wine","price":138},{"name":"meat","price":15},{"name":"water","price":1}]
son=2
ls=[]
while son:
    Max=0
    Max_x=""
    for x in bigger_price:
        if x["price"]>Max and x not in ls:
            Max=x["price"]
            Max_x=x
    ls.append(Max_x)
    son-=1
print(ls)