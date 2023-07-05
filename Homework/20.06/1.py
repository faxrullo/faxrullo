import os
os.system("cls")
class calculator:
    def __init__(self):
        self.cal=0
    def get_counter(self):
        print(f"cal = {self.cal}")
    def add_cal(self):
        self.cal+=1

    def devorse_cal(self):
        if self.cal>=0:
            self.cal-=1
        else:
            print(f"The counter can be negative:{self.cal}")
c=calculator()
while 1:
    m=input("enter the action{+/-}: ")
    if m=="-":
        c.devorse_cal()
    elif m=='+':
        c.add_cal()
    else:
        print(f"you entered the wrong action:{m}")
    c.get_counter()
    if int(input("will you continue again:{0/1}: ")):
        continue
    else:
        break
