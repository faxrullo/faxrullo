import os
os.system("cls")
class telephone:
    def __init__(self):
        self.model=""
        self.price=0
        self.color=""
        self.camera=0
    def input_data(self):
        self.model=input("Telephone modelini kiriting: ")
        self.price=int(input("Telephone narxini kiriting: "))
        self.color=input("Telephone rangini kiriting: ")
        self.camera=int(input("Telephone camerasini kiriting: "))
    def show(self):
        if self.camera > 15 and self.camera < 25:
            print("Modeli: ",self.model)
            print("Rangi: ",self.color)
            print("Narxi: ",self.price)
            print("Camerasi: ",self.camera)
n=telephone()
n.input_data()
n.show()