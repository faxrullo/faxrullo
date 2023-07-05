import os
os.system("cls")
class TriangleChekcer:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_triangle(self):
        if self.a<0 and self.b<0 and self.c<0:
            return f"{self.a},{self.b} va {self.c} lardan manfiy"
        elif (self.a+self.b>self.c) and (self.a+self.c>self.b) and (self.c+self.b>self.a):
                return f"{self.a},{self.b} va {self.c} lardan Uchburchak yasash mumkin"
        else:
            return f"{self.a},{self.b} va {self.c} lardan Uchburchak yasash mumkin emas"

t=TriangleChekcer(13,4,5)
print(t.is_triangle())