import os
os.system("cls")
class battery:
    def __init__(self):
        self._zaryad=100
    @property
    def name(self):
        return self._zaryad
    @name.setter
    def name(self,x):
        self._zaryad=x
    @name.deleter
    def name(self):
        print("Power off")
        del self._zaryad
b=battery()
print(b.name)
b.name=30
print(b.name)
del b.name
'''try:
    print(b.name)
except:
    print("Zaryad o'chgan")'''