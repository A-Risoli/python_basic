'''
Created on 16/mar/2015

@author: antonio
'''
n={}
die={'age':19, 'instrument':'trombone'}
nel={'age':21, 'instrument':'clarinet'}
sal={'age':18, 'instrument':'trombone'}
fra={'age':40, 'instrument':'euphonium'}
ant={'age':22, 'instrument':'trombone'}
mik={'age':21, 'instrument':'sax'}
people={'Diego':die,'Nello':nel,'Salvatore':sal,'francesco':fra,'Michele':mik, 'Antonio':ant}

s=raw_input("find_instrument ")

for a,b in people.items():
    if s==b['instrument']:
        n[a]=b
print n



