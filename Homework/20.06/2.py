import os
os.system("cls")
class restaurant:
    def __init__(self,name,adress,rating,capacity,type_food):
        self.name=name
        self.adsess=adress
        self.rating=rating
        self.capacity=capacity
        self.type_food=type_food
    def show_info(self):
        print("Name: ",self.name)
        print("Adress: ",self.adsess)
        print("Rating: ",self.rating)
        print("Capacity: ",self.capacity)
        print("Type_food: ",self.type_food)
    def milli_taom(self):
        if self.type_food.lower()=="milliy_taom":
            print("Name: ",self.name)
            print("Adress: ",self.adsess)
            print("Rating: ",self.rating)
            print("Capacity: ",self.capacity)
n=int(input("Restoranlar soni kiriting: "))
while n:
    r=()
    ls=list(map(str,input("Samaliyot haqida ma'lumot beirng: ").split()))
    a=restaurant(ls[0],ls[1],ls[2],ls[3],ls[4])
    a.show_info()
    a.milli_taom()
    n-=1