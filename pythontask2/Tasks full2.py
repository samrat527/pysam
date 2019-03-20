##Dictionaries

##1) Write a program to add Key-Value pair to dictionary?

##f=int(input("Enter the length:"))
##mykeys=[]
##for i in range (f):
##    s=int(input('Enter the keys:'))
##    mykeys.append(s)
##myvalues=[]
##for i in range (f):
##    d=input('Enter the values:')
##    myvalues.append(d)
    
##mydict= dict(zip(mykeys,myvalues))

##mydict={}
##for i in range (len(myvalues)):
##    mydict[mykeys[i]]=myvalues[i]

##print(mydict)

##2) Write a program to concatenate two dictionaries into one dictionary?

##d1={4:'hi', 5:'bye', 6:'howdy'}
##d2={7:'good',8:'bad'}
##
##d3=dict(d1)
##d3.update(d2)
##print(d3)

##3) Write a Python program to iterate over dictionaries using for loops.
##d1={4:'hi', 5:'bye', 6:'howdy'}
##for i in d1:
##    print(i)


##4) Write a Python script to generate and print a dictionary that contains a number(between 1 and n) in the form (x,x*x)

##l=int(input('Enter a length'))
##keys=[]
##for i in range (l):
##     numb=int(input("Enter an element:"))
##     keys.append(numb)
##
##values=[]
##for i in keys:
##    values.append(i**2)
##
##mydict={}
##if len(keys)==len(values):
##    for i in range(len(keys)):
##        mydict[keys[i]]= values[i]
##print(mydict)

##5) Write a program to remove key from the dictionary?

##d1={4:'hi', 5:'bye', 6:'howdy'}
##d=d1.pop(5)
##print(d)
##print(d1)

##6) Write a program to sort a dictionary by key?

##d1={4:'hi', 5:'bye', 6:'howdy', 10:'python', 8:'java', 1:'c++'}
##d1=dict(sorted(d1.items()))
##print(d1)


##Lists


##1) Write a program to find second largest number in a list?

##a=[]
##n=int(input('Enter length:'))
##for i in range (0,n):
##    b=int(input('Enter element:'))
##    a.append(b)
##a.sort()
##print(a)
##print('Second largest elemenet is:' , a[n-2])

##2) Write a program for calculating Mode of list numbers?

##import statistics
##
##l=int(input("Enter a length:"))
##mylist=[]
##for i in range (l):
##    num=int(input("Enter a number:"))
##    mylist.append(num)
##print(mylist)
##
##mode1=statistics.mode(mylist)
##print(mode1, "is mode")


##3) Write a program to remove the duplicate items from the list?

##mylist=[1,1,12,32,32,43,434,54,32,23]
##print(list(set(mylist)))


##4) Lets say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
##Write one line of Python that takes this list a and makes a new list that has only the even
##elements of this list in it.

##a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##
##malist=[i for i in a if i%2==0]
##print(malist)

##5) Write a program to add two matrices?????

##x=[5,6,7]
##y=[10,32,43]
##sums=[]
##for i in range (len(x)):
##    s=x[i]+y[i]
##    sums.append(s)
##print (sums)
        

##6) Write a program to display multiplication table?

##num=12
##
##for i in range (1,11):
##    print(num, 'X' ,i,'=', num*i)


##Sets

##1) Write a program to display all letters in Two string but not in Both?

##s1=set(input('Enter a string one:'))
##s2=set(input('Enter a string two:'))
##a=list((s1)^(s2))
##
##print(a)


##a= list(set(s1)^set(s2))
##print("The letters are:")
##
##for i in a:
##    print(i)

##2) Write a program to count number of vowels present in a string using sets?

##stmt=str(input("Enter a stmt"))
##vowels=set('aeiouAEIOU')
##count=0
##for i in stmt:
##    if i in vowels:
##        count=count+1
##print (count)



##3) Write a program to create symmetric difference?

##a={1,2,4,6,7,8,10}
##b={1,3,5,9,25}
##print(set(a)^set(b))




##4) Write a program to use of frozen sets?


##5) Write a program for adding element in sets?

##emptyset=set(())
##emptyset.add('Hello')
##print(emptyset)

##mixset={'hi','php'}
##mixset.add("lenovo")
##print(mixset)

##Tuples


##1) Write a program to create tuple with different data types?

##mixed=('hi', 'people', 45,54.4,35, False)
##print(mixed)


##2) Write a program that display index and value side by side?

##mixed=(1, 4, 45,54.4,35, 5)
##mylist=list(mixed)
##for i in range (len(mylist)):
##    print(i,'index - ', mylist[i])

    

##3) Write a program to convert tuple to a string?

##tup=('h','e','l','l','o')

##for i in tup:
##    print(i,end='')

##str=''.join(tup)
##print(str)

##4) Write a program to reverse a string?

##string=('hello people')
##print(string[::-1])

##5) Write a Python program to count the elements in a list until an element is a tuple?

mylist=[1,2,3,4, (1,2,4), 'python']
count=0
for i in mylist:
    if type(i) is tuple:
        break
    count=count+1
print(count)
    
        

##6) Write a program to remove an item from the tuple?

##tup=('h','e','l','l','o')
##mylist=list(tup)
##mylist.remove('o')
##print(tuple(mylist))
