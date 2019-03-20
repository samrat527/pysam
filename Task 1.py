##time=input("enter a time in AM/PM")
####if time("%I : %M : %S %a") 
##print(time.strftime("%I : %M : %S"))


time=input("enter a time in AM/PM")
if time[:-2] == 'AM' and time [:2] < '12':    
        print(time.rstip("AM"))

