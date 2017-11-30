"Python Program to Check Armstrong Number"
a=raw_input("Enter number:")

s=0
for i in a:
    s=s+int(i)**len(a)
if s==int(a):
    print "armstrong number"
else:
    print "not a armastrong number"
