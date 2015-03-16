'''
Created on 16/mar/2015

@author: antonio
'''
i=['aba', 'xyz', 'c','dd', 'bbb']
n=0
for t in i:
    p=len(t)
    if p>=2:
        if t[0]==t[p-1]:
            n+=1
print n            