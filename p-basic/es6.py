'''
Created on 16/mar/2015

@author: antonio
'''

i=['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
j=[]
for s in i:
    if s[0]=='x':
        j.append(s)
        i.remove(s)
i.sort()
j.sort()

j+=i
print j
        