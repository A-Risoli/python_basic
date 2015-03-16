'''
Created on 15/mar/2015

@author: antonio
'''
a=int(raw_input("Insert a number "))

for i in range(2,a):
    t=a%i
    if t==0:
        print a," isn't prime"
        quit()
print "Yes"