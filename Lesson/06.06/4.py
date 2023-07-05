import os
os.system("cls")
def juft_son(n):
    if n==2:
        return 2
    return n+juft_son(n-2)
n=int(input("n ="))
if n%2:
    print(juft_son(n-1))
else:
    print(juft_son(n))