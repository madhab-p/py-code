'''
Created on Apr 11, 2017

@author: pneela
'''

def findall(L,value,start=0):
    ''' Generator version of finding all occurances of value in L'''
    i = start - 1
    try:
        while 1:
            i = L.index(value,i+1)
            yield i
    except ValueError:
        pass
    
L = ['a','a','aa','cc','b','a',1,2,1,1,3]

if L.count(1) > 0:
    for ind in findall(L, 1):
        print("match at ", ind)
else:
    print('No occurance of 1')

try:
    print(L.index('aaa'))
except ValueError:
    print('aaa not found')