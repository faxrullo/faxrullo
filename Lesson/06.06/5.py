import os
os.system("cls")
def function_fibo(son,f1=0,f2=1):
    if son<f1:
        return 
    print(f1)
    f=f1+f2
    f1=f2
    f2=f 
    return function_fibo(son,f1,f2)
function_fibo(35)