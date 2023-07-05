import os
os.system("cls")
class shape:
    def __init__(self,shape_type,a):
        self.shape_type=shape_type
        self.a=a
    def show_info(self):
        print(f"{self.shape_type} shape")
    def perimetr(self):
        print(f"{self.shape_type} perimetri")
    def yuza(self):
        print(f"{self.shape_type} yuza")
class triangle(shape):
    def __init__(self,shape_type,a,b,c):
        super().__init__(shape_type,a)
        self.b=b
        self.c=c
    def show_info(self):
        super().show_info()
    def perimetr(self):
        return super().perimetr()
        print(self.a+self.b+self.c)
    def yuza(self):
        return super().yuza()
        print(self.a*self.b)
class rectangle(shape):
    def __init__(self,shape_type,a,b):
        self.b=b
    def show_info(self):
        super().show_info()
    def perimetr(self):
        return super().perimetr()
        print(2*(self.a+self.b)
    def yuza(self):
        return super().yuza()
class square(shape):
    def show_info(self):
        super().show_info()
    def perimetr(self):
        return super().perimetr()
    def yuza(self):
        return super().yuza()