import os
from datetime import *
os.system("cls")
brithday=input("Tug'ulgan sanani kiriting: ")
brithday=datetime.strptime(brithday,"%d-%m-%Y")
'''print(abs((datetime.now()-brithday).days))
brithday=brithday+timedelta(days=20)
brithday=datetime.strftime(brithday,"%d.%m.%b")
print(brithday)
print(datetime.now())'''
day=datetime.now()
print(datetime.strftime(day,"%y"))
print(datetime.strftime(brithday,"%B"))