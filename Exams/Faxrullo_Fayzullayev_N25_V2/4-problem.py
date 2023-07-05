import os
os.system("cls")
data=input("Sana va vaqtni kiriting: ")
data=data.split()
day=data[0].split(".")
time=data[1].split(":")
st=day[0]
match int(day[1]):
    case 1:
        st+=" Yanvar "
    case 2:
        st+=" Fevral "
    case 3:
        st+=" Mart "
    case 4:
        st+=" Aprel "
    case 5:
        st+=" May "
    case 6:
        st+=" Iyun "
    case 7:
        st+=" Iyul "
    case 8:
        st+=" Avgust "
    case 9:
        st+=" Sentabr "
    case 10:
        st+=" Oktabr "
    case 11:
        st+=" Noyabr "
    case 12:
        st+=" Dekabr "
st+=day[2]+" years "+time[0]+" hours "+time[1]+" minutes"
print(st)   