import os
os.system("cls")
class mashina:
    def __init__(self,m,p,c):
        self.modeli=m
        self.price=p
        self.color=c
    def show(self):
        print("Modeli: ",self.modeli)
        print("Rangi: ",self.color)
        print("Narxi: ",self.price)
class yengil_mashina(mashina):
    pass
m=input("Mashina modelini kiriting: ")
p=int(input("Mashina narxini kiriting: "))
c=input("Mashina rangini kiriting: ")
car=yengil_mashina(m,p,c)
car.show()