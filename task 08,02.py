#Task3
mylist=["2103","python",[342, 4324],5242,["english","hi"]]
newlist=[]
for i in mylist:
    if type(i) ==list:
        for j in i:
            newlist.append(j)
    else:
        newlist.append(i)
print(newlist)

    



#Task2
mylist=[2103,"python",342, 4324,5242,"english"]
lstr=[]
lint=[]
for i in mylist:
    if type(i)==str:
        lstr.append(i)
    else:
        lint.append(i)
print(lstr)
print(lint)

#Task2
l=int(input("Enter a length:"))
lint=[]
lstr=[]
for i in range(l):
    print('''1.Integer
2. String''')
    dt=int(input("enter the datatype:"))

    if dt==1:
        ele=int(input("enter the number:"))
        lint.append(ele)
    elif dt==2:
        ele=input("enter a string:")
        lstr.append(ele)
    else:
        print ("enter a correct option:")

print(lint)
print(lstr)

##l=input("Enter elements for the list :")
##mylist=[]
##for i in l:
##    lint[type(i)].append(i)
##
##print (mylist[int])
##print (mylist[str])

#Task1
l=int(input("Enter a length of the list :"))
l1=[]
for i in range (l):
    num=int(input("Enter a number for list one: "))
    l1.append(num)
l2=[]
for i in range (l):
    num=int(input("Enter a number for list two: "))
    l2.append(num)
sum=[]
for i in range(l):
    s=l1[i]+l2[i]
    sum.append(s)
print(sum)
