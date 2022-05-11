import os
from os import system, name
import smtplib
import time
from time import sleep


def clear_console():
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

 # At First we have to get the current CPU-Temperature with this defined function  
def getCPUtemperature():  
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').read()  
    return(res.replace("temp=","").replace("'C\n",""))
    

#https://github.com/padelt/temper-python
def gettemperature():  
    res = os.popen('/home/pi/.local/bin/temper-poll').read()
    possalto=res.find(':')
    return(res[possalto+2:31:1])  

while True:
    clear_console()
    print("Room: "+str(gettemperature())   +" ºC")
    print("CPU:  "+str(getCPUtemperature())+" ºC")
    time.sleep(0.5)
    
