import os
os.system("cls")
class computer:
    def __init__(self):
        self.name=""
        self.RAM=0
        self.price=0
        self.protsessor=""
    def init_data(self):
        self.name=input("Computer name: ")
        self.price=int(input("Computer price: "))
        self.RAM=int(input("Computer RAM: "))
        self.protsessor=input("Computer protsessor: ")
    def show(self):
        if self.RAM>=4 and self.RAM<=16:
            print("Computer name: ",self.name)
            print("Computer RAM: ",self.RAM)
            print("Computer price: ",self.price)
            print("Computer protsessor: ",self.protsessor)
            print("-"*35)
n=int(input("how many computers do you enter? "))
computers=[]
for x in range(n):
        c=computer()
        print(f"{x+1} - computer")
        c.init_data()
        computers.append(c)
os.system("cls")
for x in range(n):
     computers[x].show()