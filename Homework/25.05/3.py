import os
os.system("cls")
A,B,C = map(int,input("Sonlarni kiriting: ").split())
A,B,C = C,A,B
print("Natija: A={0}, B={1}, C={2}".format(A,B,C))