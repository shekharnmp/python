"Python Program to Find Armstrong Number in an Interval"
a = int(raw_input("Enter a number:"))
b = int(raw_input("Enter b number:"))
for num in range(a,b+1):
    num1=len(str(num))
    s=0
    for x in str(num):
        s = s+int(x)**num1
    if s == num:
        print "Armstrong numbers is: {0}".format(num)
