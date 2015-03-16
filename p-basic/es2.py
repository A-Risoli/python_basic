'''
Created on 16/mar/2015

@author: antonio
'''
a=int(raw_input("Insert the livel "))
f1=1
f2=1

for i in range(a):
    g=f1
    print f1
    f1=f1+f2
    f2=g
    