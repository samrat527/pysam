##Task 1

time=input("enter a time in AM/PM")
if time[-2:] == 'AM' and time [:2] < '12':
 print(time.rstrip("AM"))
elif time[-2:] == 'AM' and time [:2] == '12':
 print (time.replace(time[:2] , '00').rstrip ('AM'))  
elif time[-2:] == 'PM' and time [:2] != '12':
 print(str(int(time[:2]) + 12) + time[2:8])
elif time[-2:] == 'PM' and time [:2] == '12':
 print (time.rstrip("PM"))
else:
 print("wrong format of input")

##Task 2
stmt=input("enter an input")
if stmt.isalpha():
    print("length of " + stmt + " is " + str(len(stmt)))
elif stmt.isdigit():
    print("square of " + stmt + " is " , int(stmt)**2)

