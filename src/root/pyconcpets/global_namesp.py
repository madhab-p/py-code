'''
Created on Apr 11, 2017

@author: pneela
'''
globvar = 100
print('Gloabl value ', globvar)

def fun1():
    '''glbavar is restriced to function scope'''
    
    globvar = 101
    print('Inside fun1' , globvar)

def fun2():
    '''change the global variable inside the function'''
    global globvar 
    globvar = 111
    print('Inside fun2' , globvar)
    
    
fun1()
print('Outside fun1', globvar)
fun2()
print('Outside fun2', globvar)