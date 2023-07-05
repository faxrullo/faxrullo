import   os
os.system("cls")
a=int(input("Sonni kiriting: "))
try: 
    print(f"{10/a}")
except:
    print("Siz nolni kiritidingiz")
else:
    print("Siz to'g'ri sonni kiritdingiz")
finally: 
    print("Sizni dasturiz ishladi ")