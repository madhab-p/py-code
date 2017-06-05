'''
Created on Apr 10, 2017

@author: pneela
'''

class Test(object):
    
    def method(self,i):
        if i < 10:
            print(i)
            i += 1
            self.method(i)

if __name__ == '__main__':
    Test().method(0)

'''
a = [22,333,44,222,55,55,222,222]


#Enumerate - packages an index and value into a touple
for i,v in enumerate(a):
    print(i,v)

def double(n):
    return 2 * n

obj = map(double, a)


i = -1
try:
    while 1:
        i = a.index(222, i+1)
        print('Match found at : ',i )
        yield
except ValueError:
    pass

'''