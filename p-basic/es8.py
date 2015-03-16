'''
Created on 16/mar/2015

@author: POLITO\s192867
'''

def purge(a):
    
    b=a.replace(".","")
    b=b.replace("*","")
    b=b.replace(",","")
    b=b.replace("?","")
    b=b.replace("!","")
    b=b.replace("-","")
    b=b.replace(":","")
    b=b.replace(";","")
    b=b.replace("'","")
    b=b.replace("\"","")
    b=b.replace("`","")
    b=b.lower()

    return b
    
    
def main():
    d={}
    txt=open(raw_input("Insert a file name "))
    s=txt.read().split()
    for f in s:
        
        f=purge(f)
        if f in d:

            d[f]+=1
        else:
                d[f]=1

    for a,b in d.items():
        print a, b
        


    

if __name__=='__main__':
    main()

    