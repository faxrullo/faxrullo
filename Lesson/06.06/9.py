import os
os.system("cls")
def count_digits(st):
    count=0
    for x in st:
        if ord(x)>=48 and ord(x)<=57:
            count+=1
    return count
st=input("Satrni kiriting: ")
print(count_digits(st))