import os
os.system("cls")
class soliq:
    def __init__(self):
        self.clients=[]
        self.name=""
        self.age=0
        self.sex=""
        self.number_phone=""
        self.email=""
        self.password=""
        self.adress=""
        self.pasport_number=""
    def sign_up(self):
        self.name=input("name:")
        self.age=input("age:")
        self.sex=input("sex:")
        self.number_phone=input("number phone:")
        self.email=input("email:")
        self.password=input("password:")
        self.adress=input("adress:")
        self.pasport_number=input("pasport number:")
        self.clients.append([self.name,self.age,self.sex,self.number_phone,self.email,self.password,self.adress,self.pasport_number])
    def log_in(self):
        email=input("enter the email")
        password=input("enter the password")
        for x in self.clients:
            if x[4]==email and x[5]==password:
                print("Siz tizimga kirdingiz")
                self.__main_menu(email)
            else:
                print("Login yoki parol xato kiritildi")
    def __main_menu(self,email):
        print("1.show info")
        print("2. Parolni o'zgartirish")
        x=int(input("Yuqoridagilardan birini tanlang: "))
        if x==1:
            self.show_clients(email)
        else:
            pas=input("Yangi parolni kiriting: ")
            for x in self.clients:
                if x[4]==email:
                    x[5]=pas
        self.show_clients()
    def show_clients(self,email):
        for x in self.clients:
            if x[5]==email:
                print(x)
            
o_n=soliq()
o_n.sign_up()
o_n.sign_up()
o_n.log_in()
            