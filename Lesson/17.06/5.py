import os
os.system("cls")
class shape:
    def show(self,s):
        print(f"{s} shakl")
class uchburchak(shape):
    pass
class tortburchak(shape):
    pass
class kvadrad(shape):
    pass
class aylana(shape):
    pass
shakl=input("Shaklni kiriting: ")
if shakl=="aylana":
    s=aylana()
    s.show(shakl)
elif shakl=="kvadrad":
    s=kvadrad()
    s.show(shakl)
elif shakl=="tortburchak":
    s=tortburchak()
    s.show(shakl)
elif shakl=="uchburchak":
    s=uchburchak()
    s.show(shakl)
else:
    s=shape()
    s.show(shakl)