import os
os.system("cls")
class team:
    def __init__(self):
        self.name=""
        self.number_of_participants=0
        self.coach=""
        self.captain=""
    def init_data(self):
        self.name=input("Team name: ")
        self.number_of_participants=int(input("Team number of participants: "))
        self.coach=input("Team coach: ")
        self.captain=input("Team capatian: ")
    def show(self):
        print("Team name: ",self.name)
        print("Team number of participants: ",self.number_of_participants)
        print("Team coach: ",self.coach)
        print("Team captain: ",self.captain)
    def check(self):
        sch=0
        if self.name.lower()=="new_komanda":
            sch+=1
        return sch
n=int(input("how many teames do you enter? "))
teams=[]
for x in range(n):
    print(f"\n\t{x+1} - enter team information")
    t=team()
    t.init_data()
    teams.append(t)
for x in range(n):
    print(f"\n\t{x+1} - team information")
    teams[x].show()
sch=0
for x in range(n):
    if teams[x].check():
        print("\n\tTeam name=='New_komanda")
        teams[x].show()
        sch+=1
if sch==0:
    print("\n\tBunday jamoa mavjud emas")
