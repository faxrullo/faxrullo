import os
os.system('cls')
class Uzum_bank:
    def __init__(self):
        self._name=None
        self._surname=None
        self._birthday=None
        self._jshshir=None
        self._email=None
        self._email_password=None
        self._users=list()
    
    def sign_up(self):
        print("Ro'yxatdan o'tish uchun quyidagilarni to'ldiring: ")
        self._name=input("Ismni: ")
        self._surname=input("Familiya: ")
        self._birthday=input("Tug'ilgan sana: ")
        self._jshshir=int(input("JSHSHIR: "))
        self._email=input("Email: ")
        self._email_password=input("Email password: ")
        self._users.append([self._name,self._surname,self._birthday,self._jshshir,self._email,self._email_password])
        self._users=str(self._users)
        f=open("Foydalanuvchilar.txt",'a+')
        f.write(self._users)
        f.write("\n")

    def main_menu(self):
        print(f"\t\t1.Asosiy\n\t\t2.O'tkazma\n\t\t3.To'lov\n\t\t4.Chat\n\t\t5.Menyu\n\t\t6.Sozlamalar")
        temp=int(input())
        match (temp):
            case 1:
                self._asosiy()
            case 2:
                self._otkazmalar()
            case 3:
                self._tolov()
            case 4:
                self._chat()
            case 5:
                self._menyu()
            case 6:
                self._sozlamalar()

    def _asosiy(self):
        os.system("cls")
        n=len(Card._cards)
        while n:
            print(f"Karta nomi: {Card._card_name}\tKarta hisobi: {Card._card_balance}")
            n-=1

    def _otkazmalar(self):
        os.system("cls")
        print("\t1.Kartaga o'tkazma\n\t2.Hamyonga o'tkazma\n\t3.Hisob raqamga o'tkazma\n\t4.Rekvizitlar bo'yicha to'lash\n\t5.Raketa")
        temp=int(input())
        match(temp):
            case 1:
                n=1
                for x in Card._cards:
                    print(f"{n}.{x}")
                    n+=1
                k=int(input("Kartalarizdan birini tanglag: "))
                f=open("Foydalanuchilar_kartalari.txt",'r+')
                ls=f.readline()
                ls=ls.split()
                print(ls)
                c=(input("To'lov qilinadigan kartani kiriting: "))
                for x in range(len(ls)):
                    if ls[x][1]==c:
                        print("salom")
                        ls[x][2]+=int(input("To'lov summasi: "))
        
                        

    def _tolov(self):
        pass

    def _chat(self):
        pass

    def _menyu(self):
        pass

    def _sozlamalar(self):
        pass
class Card:
    _card_balance=None
    _card_name=None
    _cards=dict()
    def __init__(self):
       pass

    def sign_up_card(self):
        print("Ilovaga karta qo'shmoqchi bo'lsangiz quyidagilarni to'ldiring: ")
        f=open("Kartlar.txt","a+")
        Card._card_name=input("Karta nomi: ")
        f.write(Card._card_name)
        f.write(": ")
        Card._card_balance=int(input("Karta hisobi: "))
        f.write(str(Card._card_balance))
        f.write("\n")
        Card._cards[Card._card_name]=Card._card_balance
    
    def show_balanace_card(self,name):
        for x in Card._cards:
            if x==name:
                print(f"{x}: {Card._cards[x]}")

c=Card()
c.sign_up_card()
c.sign_up_card()
#c.show_balanace_card("humo")
u=Uzum_bank()
u.main_menu()
#u.sign_up()