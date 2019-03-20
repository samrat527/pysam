##Conditional Statements
##1) Write a program for grading system of marks?
##stu=int(input("Enter a number of students:"))
##for i in range(stu):
##        grader=int(input("Please enter the mark:"))
##        if grader>=60 and grader<=70:
##            print("D")
##        elif grader>70 and grader<=80:
##            print("C")
##        elif grader>80 and grader<=90:
##            print("B")
##        elif grader>90 and grader<=100:
##            print("A")
##        else:
##            print("Fail")
##2) Write a program that check for leap year?

##year=int(input("Enter a year:"))
##if year%4==0:
##    print("%d is leap year" %(year))
##else:
##    print("%d is not a leap year" %(year))

##3) Write a program that checks the number is even or odd?

##numb=int(input("Enter a number:"))
##if numb%2==0:
##    print("%d is even number" %(numb))
##else:
##    print("%d is odd number" %(numb))

##4) Write a program that takes country, state and print number of districts by users?




##5) Write a program for finding largest of Three numbers?

##num1=int(input("Enter the first number:"))
##num2=int(input("Enter the second number:"))
##num3=int(input("Enter the third number:"))
##
##if num1>num2 and num1>num3:
##    lrgst=num1
##elif num2>num1 and num2>num3:
##    lrgst=num2
##else:
##    lrgst=num3
##print("%d is the largest number" %(lrgst))

##Control Flow

##1) Write a program for printing number in the range excluding that are multiples of 3 and 5?

##num=int(input("Enter a number:"))
##for i in range(num):
##    if i%3!=0 and i%5!=0:
##        print(i, end = ' ')

##2) Write a program that prints only the even numbers squares in the specified range?

##user=int(input('Enter a number:'))
##for i in range (1,user+1):
##    if i%2==0:
##        print(i**2)

##3) Write a program that prints only the odd numbers that are divisible by 7 between 1
##to 100 using control flows?

##for i in range (1,101):
##    if i%2!=0 and i%7==0:
##        print(i)
        
##4) Write a program that print all vowels in the input string using control flow
##statements?

##stmt=input("Enter a stmt")
##vowels='aeiou'
##for i in stmt:
##      if i.lower() in vowels:
##          print (i)


##Looping

##1) Write a program that checks whether the specified number is Armstrong number?

#if it is 4 digits

##num=input('Enter a number:')
##if int(num)==1 or int(num)==0:
##    print("Armstrong number")
##elif int(num[0])**3+int(num[1])**3+int(num[2])**3==int(num):
##    print("Armstrong number")
##else:
##    print("not an Armstrong number")

##2) Write a program to that checks the number is a prime or not?

##user=int(input("enter a number:"))
##for i in range (2,user):
##     if user%i==0:
##         print("not Prime")
##         break
##if i==user-1:
##     print("Prime")


##3) Write a program for printing first 10 Fibonacci sequence?

##first=0
##scnd=1
##for i in range(0,10):
##    print(first , end = ' ')
##    s=first
##    first=scnd
##    scnd=s+scnd




##4) Write a program for odd even count between range?
##in a range separate odd and even numbers

##num=int(input("Enter number:"))
##even=[]
##odd=[]
##for i in range (1, num+1):
##    if i%2==0:
##       even.append(i)
##print(even,'even numbers')
##for i in range (1, num+1):
##    if i%2!=0:
##        odd.append(i)
##print(odd, 'odd numbers')



##5) Write a program for print the following pattern?
##user_input=int(input("enter a number:"))
##for i in range(user_input,0,-1):    
##    print("*"*i)

##6) Write a program for multiples of 9 using if?
##num=int(input('Enter a number:'))
##for i in range(1,num+1): can be in range?
##if num%9==0:
##    print("%s is multiples of 9" %(num))
        
##7) Write a program for printing numbers that are in the range between 1 to 50 and divisible
##by either 2 or 3?
##for i in range(1,50):
##    if i%2==0 or i%3==0:
##        print(i)

##8) Write a program to calculate sum of digits in number?

##num=int(input('Enter a number:'))
##s=0
##while num>0:
##    dig=num%10
##    s=s+dig
##    num=num//10
##print("Total sum of digits is: " , s)

##Strings

##1) Write a program for printing "yhnetobgnes" from "pythonbestforbeginners".
##stmt = "pythonbestforbeginners"
##print(stmt[1:22:2])

##2) Write a program to print reverse of a user given string.

##stmt=input("Enter a statement")
##print(stmt[::-1])

##3) Write a program to change all occurances of 3rd charecter with '@'?

##stmt=input("Enter a statment")
##
##print(stmt.replace(stmt[2], '@'))

##4) Write a program to replace a string with new string only specified number of times?

##stmt = ("Python is easy language. Python is easy to learn")
##print(stmt.replace('Python' , 'Java'))

##5) Write a program to print character that are at multiples of 3 position in a user input string?

##stmt=str(input("Enter a statement:"))
##print(len(stmt))
##for i in range(1,len(stmt)):
##    if i%3==0:
##        print(stmt[i])

##6) Write a program that exchange value of two numbers without using temporary variable.


##a=10
##b=20
##a,b=b,a
##
##print(a)
##print(b)


##Variables and Data types

##1) Write a program to check whether the given string present in the sequence or not.

##L=['digital' , 'lync', 'gachiwboli', 23, 'hyd']
##print('hyd' in L)


##2) Write a python program to perform all bitwise operations for given values:

##a=45
##b=65
##print(a&b)
##print(a|b)
##print(~a)
##print(a^b)
##print(a>>1)
##print(a<<1)

##3) Convert the given value into integer, double, complex and calculate absolute value,
##factorial, square root, exponent of that value.

##z=65.33

##print(int(z))
##print(float(z))
##print(complex(z))
##
##print(abs(z))

##x=65
##factorial=1
##for i in range(1,66):
##    factorial=factorial*i
##print(factorial)

##print(65!)

##import math
##a=math.sqrt(z)
##print(a)
##
##print(z**2)
    
##4) Write a Python program to calculate the sum of the digits in an integer.

##num=int(input('Enter a number:'))
##s=0
##while num>0:
##    dig=num%10
##    s=s+dig
##    num=num//10
##print("Total sum of digits is: " , s)


##5) Write an program that perform all comparison operation to following two values 15 and 2?

##a=15
##b=2
##print(a==b)
##print(a!=b)
##print(a>b)
##print(a>=b)
##print(a<=b)
##print(a<b)
