import os
from abc import ABC,abstractmethod
os.system("cls")
class Najot_talim(ABC):
    def __init__(self):
        self.name_branch=None
        self.year_found=None
        self.adress=None
        self.count_pupil=None
        self.count_room=None
    @abstractmethod
    def input_data(self,n,y,a,p,r):
        self.name_branch=n
        self.year_found=y
        self.adress=a
        self.count_pupil=p
        self.count_room=r
    @abstractmethod
    def show_data(self):
        print(f"Name: {self.name_branch}\nYear found: {self.year_found}\nAdress: {self.adress}\nCount pupil: {self.count_pupil}\nCount room: {self.count_room}")

class Chimboy(Najot_talim):
    def __init__(self):
        super().__init__()
    def input_data(self, n,y, a, p, r):
        super().input_data(n,y, a, p, r)
    def show_data(self):
        super().show_data()
class Xadra(Najot_talim):
    def __init__(self):
        super().__init__()
    def input_data(self, n,y, a, p, r):
        super().input_data(n,y, a, p, r)
    def show_data(self):
        super().show_data()
ch=Chimboy()
ch.input_data("Chimboy",2019,"Olmazor",500,10)  
ch.show_data()
print("-"*35)
x=Xadra()
x.input_data("Xadra",2018,"Chorsu",1000,20)
x.show_data()