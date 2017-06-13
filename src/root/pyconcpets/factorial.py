'''
Created on Apr 11, 2017
Synopsis:
    This document exhibits how doctest module can be used
    for testing of the module.

@author: pneela
'''

def factorial(x):
    '''
    >>> factorial(5)
    120
    
    This function should not be called with very a large number
    >>> factorial(1329283)
    Traceback (most recent call last):
    ...
    RecursionError: maximum recursion depth exceeded in comparison
    
    No -ve number for factorial
    >>> factorial(-4)
    Traceback (most recent call last):
    ...
    ...
    ValueError: n must be >= 0
    '''
    if x < 0:
        raise ValueError('n must be >= 0')
    if x ==1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    print(factorial(10))