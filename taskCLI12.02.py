import sys
print(sys.argv)

if len(sys.argv)==2:
    if sys.argv[1].isdigit():
        l=int(sys.argv[1])
        mylist=[]
        for i in range(1,l+1):
            mylist.append(i)
        print(mylist)
        sq=[i**2 for i in range(1,l+1)]
        print(sq)
    else:
        print("Enter a digit:")
else:
    print("Entered multiple elements")

#second version of the Task 1

##import sys
##print(sys.argv)
##
##if len(sys.argv)==2:
##    if sys.argv[1].isdigit():
##        l=int(sys.argv[1])
##        mylist=[]
##        for i in range(1,l+1):
##            mylist.append(i)
##        print(mylist)
##        lsq=[]
##        for i in range(1,l+1):
##            sq=i**2
##            lsq.append(sq)
##        print(lsq)
##    else:
##        print("Enter a digit:")
##else:
##    print("Entered multiple elements")
