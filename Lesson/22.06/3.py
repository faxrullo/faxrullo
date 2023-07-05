import os
os.system("cls")
class hayvon:
    def __init__(self,name,kkal):
        self.name=name
        self.kkal=kkal
   
    def show_info(self):
        print(f"{self.name}ning kkalsi {self.kkal}ga teng")

class yemish(hayvon):
    def __init__(self,name_ot,kkal_ot,name,kkal):
        super().__init__(self)
        self.name_ot=name_ot
        self.kkal_ot=kkal_ot
    def ovqalanish(self):
        if self.kkal>=100:
            print(f"Haynonni kkal {self.kkal} bo'lganigi uchun to'q")
            return 0
        else:
            self.kkal+=self.kkal_ot
h=hayvon("Ot",10)
o=yemish("o't",30)
o.ovqalanish() 
h.show_info