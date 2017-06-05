'''
Synopsis:
Understand namespace and scopes of Python.
Variable value resolution happens in the following order
    Local
        ->Enclosed
            ->Global
                ->Built-in
                

Created on Jun 1, 2017

@author: pneela
'''


def scope_test():
    def do_local():
        spam = 'local spam'
        
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    
    def do_global():
        global spam
        spam = 'global spam'
    
    spam = "test spam"
    do_local()
    print('After local assignment: ',spam)
    
    do_nonlocal()
    print('After non-local assignment: ', spam)
    
    do_global()
    print('After global assignment', spam)
    

scope_test()
print('In global scope:', spam)

