import os
os.system("cls")
class time:
    s=0
    m=0
    sec=0
    def __init__(self,s,m,sec):
        time.s=s
        time.m=m
        time.sec=sec
    def show_time(self):
        print(f"{0:02d}:{1:02d}:{2:02d}".format(time.s,time.m,time.sec))
class secund(time):
    def __init__(self):
        time.sec=time.sec+5
class minut(time):
        time.m=time.m+5+(time.c)//60
        time.sec=time.sec%60
class hour(time):
    def __init__(self):
        time.s=time.s+5+(time.m)//60
        time.m=time.m%60
t=time(5,10,15)
t.show_time()
se=secund( )
h=hour
