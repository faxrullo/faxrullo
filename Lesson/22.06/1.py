import os
os.system("cls")
class mashina:
    def __init__(self,yoqligi):
        self.__yoqilgi=yoqligi
        self.__yurgan_masofa=100
        self.__kassa=0
    def klent(self,x):
        # 1 km uchun yo'l kira 2 000 so'm
        # 1 km uchun sarflangan yoqilg'i 0.2 litr
        if self.__yoqilgi-x*0.2>0:
            self.__yoqilgi-=x*0.2
            self.__yurgan_masofa+=x
            self.__kassa+=x*2000
        else: 
            print(f"Yoqilg'iz bu masofaga borish uchun kamlik qiladi {self.__yoqilgi}")
    def kassadagi_pul(self):
        print(f"Kassada pul {self.__kassa} so'm")
    def qoldiq_yoqilgi(self):
        print(f"Mashinadagi qolgan yoqilg'i {self.__yoqilgi} litr")
    def masofa(self):
        print(f"Mashina yurgan masofasi {self.__yurgan_masofa} km")
    def zaprafka(self,k):
        self.__yoqilgi+=k
        self.__yoqilgi-=k*9000
    
m=mashina(20)
m.qoldiq_yoqilgi()
m.klent(20)
m.qoldiq_yoqilgi()
m.kassadagi_pul()
m.klent(40)        
m.qoldiq_yoqilgi()
m.kassadagi_pul()