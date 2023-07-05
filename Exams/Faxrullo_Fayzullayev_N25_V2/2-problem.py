import os
os.system("cls")
MORSE = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f",
"--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m",
"-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t",
"..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..:":"z"}
st=input("Morse kodini kiriting: ")
st=st.split(" ")
suz="" 
print(st)
for x in st:
    if x!='':
        suz+=MORSE[x]
        sch=0
    elif sch==0:
        suz+=" "
        sch+=1
print(suz)