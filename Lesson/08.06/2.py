import os
os.system("cls")
from  colorama import *
init(autoreset=True)
f_i_o=list(map(str,input("F.I.Oni kiriting: ").split()))
print(Fore.BLACK+Back.WHITE+Style.BRIGHT+f"{f_i_o[0]}")
print(Fore.BLUE+Back.RED+Style.NORMAL+f"{f_i_o[1]}")
print(Fore.MAGENTA+Back.YELLOW+Style.BRIGHT+f"{f_i_o[2]}")