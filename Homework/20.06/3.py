import os
os.system("cls")
class aeroport:
    def __init__(self,adress,fromadress,name_airplane,landing,to_fly):
        self.adress=adress
        self.fromadress=fromadress
        self.name_airplane=name_airplane
        self.landing=landing
        self.to_fly=to_fly
        self.count=0

    def landing_time(self):
        print(f"{self.name_airplane}  {self.adress}ga {self.landing}da qo'nadi")
        self.count+=1
    def fly_time(self):
        print(f"{self.name_airplane} {self.fromadress}dan {self.to_fly}da uchadi")
        self.count+=1
    def count_reys(self):
        return self.count
        
sch=0
while 1:
    ls=list(map(str,input("Samaliyot haqida ma'lumot beirng: ").split()))
    a=aeroport(ls[0],ls[1],ls[2],ls[3],ls[4])
    a.fly_time()
    a.landing_time()
    sch+=a.count_reys()
    if int(input("Yana davom etish uchun 1 bosing,aks holda 0 ni: ")):
        continue
    else:
        print(f"Bir kunlik reyslar soni {sch} ta")
        break