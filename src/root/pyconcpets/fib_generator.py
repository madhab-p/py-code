'''
Created on Apr 11, 2017

@author: pneela
'''

def fib(max):
    '''This is generator based fibonacci function'''
    a, b = 0 ,1
    while a < max:
        yield a
        a,b = b,a+b
    return

fib_fun = fib(50)
for i in fib_fun:
    print(i)

n = 100

sum_n = (i ** 2 for i in range(n))

for sq in sum_n:
    print(sq, sq ** 0.5)
