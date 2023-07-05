import os
os.system("cls")
class bus: 
    def __init__(self):
        self.passengers=0
        self.capacity=40

    def show_passengers(self):
        print(f"Passengers count: {self.passengers}")

    def empty_space(self):
        print(f"The number of vacancies is {self.capacity-self.passengers}")

    def add_passenger(self,n):
        if n+self.passengers<=self.capacity:
            self.passengers+=n
            return True
        else:
            print(f"There is room for {self.capacity-self.passengers} passengers")
            return False

    def divorce_passenger(self,n):
        if self.passengers-n>=0:
            self.passengers-=n
            return True
        else:
            print(f" {self.passengers}  passengers left")
            return False
p=bus()
while 1:
    m,n=map(str,input("Enter the method{+/-} and number of departing or disembarking passengers: ").split())
    n=int(n)
    if m=='+':
        if p.add_passenger(n)==False:
            break
    elif m=="-":
        if p.divorce_passenger(n)==False:
            break
    else:
        print("You entered the wrong character")
    p.show_passengers()
    p.empty_space()


