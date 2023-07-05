import os
os.system("cls")
class electron_saylov:
    def __init__(self):
        self._passport=None
        self._password=None
        self._name=None
        self._surname=None
        self._brithday=None
        self._adress=None
        self._age=None
        self._saylovchilar=list()
        self._ovozlar=[0,0,0,0]

    def sign_up_admin(self):
        n=int(input("Saylovchilar sonini kiriting: "))
        x=1
        while x<n:
            print(f"{x}-saylovchining ma'lumotlarini kiriting")
            self._name=input("Saylovchining ismini kiriting: ")
            self._surname=input("Saylovchining familiyasini kiriting: ")
            self._age=int(input("Saylovchining yoshini kiriting: "))
            self._brithday=input("Saylovchining tug'ulgan kunini kiriting: ")
            self._passport=input("Saylovchining passport raqami va seriyasini kiriting: ")
            self._password=input("Saylovchining JSHSHIRni kiriting: ")
            self._adress=input("Saylovchining manzilini kiriting: ")
            self._saylovchilar.append([self._passport,self._password,self._name,self._surname,self._brithday,self._adress,self._age])
            x+=1
    def saylov(self):
        password=input("JSHSHIRni kiriting: ")
        passport=input("Passport seriyasini va raqamini kiriting: ")
        for x in self._saylovchilar:
            if x[0]==passport and x[1]==password:
                print("Nomzodlardan birini tanlang:\n\t\t1.Shavkat Miromonovich MIRZIYOYEV\n\t\t2.Ulug‘bek Ilyasovich INOYATOV\n\t\t3.Robaxon Anvarovna MAXMUDOVA\n\t\t4.Abdushukur Xudoyqulovich XAMZAYEV")
                temp=int(input())
                match(temp):
                    case 1:
                        self._ovozlar[0]+=1
                        print("Siz Shavkat Miromonovich MIRZIYOYEV ovoz berdingiz")
                    case 2:
                        self._ovozlar[1]+=1
                        print("Siz Ulug‘bek Ilyasovich INOYATOV ovoz berdingiz")
                    case 3:
                        self._ovozlar[2]+=1
                        print("Siz Robaxon Anvarovna MAXMUDOVA ovoz berdingiz")
                    case 4:
                        self._ovozlar[3]+=1
                        print("Siz Abdushukur Xudoyqulovich XAMZAYEV ovoz berdingiz")
                    case _:
                        print("Bunday nomzod mavjud emas")
    def saylov_natijasi(self):
        for x in self._ovozlar:
            print(x)

s=electron_saylov()
s.sign_up_admin()
s.saylov()
s.saylov_natijasi()