import os
os.system("cls")
class notebook:
    def __init__(self):
        self.model=""
        self.price=0
        self.color=""
        self.memoriy=0
    def inputer(self):
        self.model=input("Notebook modelini kiriting: ")
        self.price=input("Notebook narxini kiriting: ")
        self.color=input("Notebook rangini kiriting: ")
        self.memoriy=input("Notebook xotirasini kiriting: ")
    def show(self):
        print("Modeli: ",self.model)
        print("Rangi: ",self.color)
        print("Narxi: ",self.price)
        print("Xotirasi: ",self.memoriy)
n=notebook()
n.inputer()
n.show()