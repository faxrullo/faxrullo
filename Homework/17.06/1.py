import os
os.system("cls")
class book:
    def __init__(self):
        self.book_name=""
        self.book_price=0
        self.book_publisher=""
        self.book_aouthor=""
    def init_data(self):
        self.book_name=input("Book name: ")
        self.book_price=int(input("Book price: "))
        self.book_publisher=input("Book publisher: ")
        self.book_aouthor=input("Book aouthor: ")
    def show(self):
        if self.book_publisher[0] in ['A','B','C','D','E','F','G','H']:
            print("Book name: ",self.book_name)
            print("Book price: ",self.book_price)
            print("Book price: ",self.book_publisher)
            print("Book aouthor: ",self.book_aouthor)
            print("-"*34)
n=int(input("how many books do you enter? "))
books=[]
for x in range(n):
    print(f"{x+1} -information")
    b=book()
    b.init_data()
    books.append(b)
os.system("cls")
for x in range(n):
    books[x].show()