import os
os.system("cls")
class country:
    def __init__(self):
        print("Country sinf ishga tushdi")
    def language(self):
        print("Davlatlar biri biri bilan davlat tili bo'yicha farq qiladi")
    def area(self):
        print("Har bir davlat o'z maydoniga ega")
class Russia(country):
    def __init__(self,name,area):
        self.name=name
        self.Area=area
        self.population=0

    def input_population(self,x):
        self.population=x
    def language(self):
        return f"{self.name}da  davlar tili Rus tili"
    def show_info(self):
        return self.population
class Canada(country):
    def __init__(self,name,area):
        self.name=name
        self.Area=area
        self.population=0

    def input_population(self,x):
        self.population=x

    def show_info(self):
        return self.population
c=Canada("Canada",250)
print(f"Aholi soni {c.input_population(50000)}")
c.show_info()
c.language()
c.area()