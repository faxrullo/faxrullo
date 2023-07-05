import os
os.system("cls")
class car:
    def __init__(self):
        self.modeli=""
        self.price=0
        self.color=""
    def input_data(self):
        self.model=input("Mashina modelini kiriting: ")
        self.price=int(input("Mashina narxini kiriting: "))
        self.color=input("Mashina rangini kiriting: ")
    def show(self):
        print("Modeli: ",self.model)
        print("Rangi: ",self.color)
        print("Narxi: ",self.price)
cars=[]
n=int(input("Mashina sonini kiriting: "))
for x in range(n):
    m=car()
    m.input_data()
    cars.append(m)
Max=cars[0]
for x in cars:
    if x.price > Max.price:
        Max=x
Max.show()