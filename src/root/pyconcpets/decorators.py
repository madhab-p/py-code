'''
Created on Apr 26, 2017
@synosis:
All about decorators.
Start reading from bottom .

@author: pneela
@reference : 
    https://realpython.com/blog/python/primer-on-python-decorators/
    https://dbader.org/blog/python-decorators
'''

# when decorator are used on a function
# it looses the meta info (such as name, scope)
# while being called from the inside of 
# a wrapper. The meta info can be preserved by 
# using functools.wrap
# Ex - 4

"""
import functools

def uppercase(func):
    def wrapper():
        return func().upper()    
    return wrapper

@uppercase
def greet_u():
    ''' Just return a greeting string'''
    return 'Hello'

# though both name and doc exist for greet()
# they will not get printed below because 
# of the wrapper function
print(greet_u.__name__)
print(greet_u.__doc__)

# above probelm can be fixed by using functools.wrap

def lowercase(func):
    # this function below copies 
    # the lost meta data
    
    @functools.wraps(func)
    def wrapper():
        return func().lower()    
    return wrapper

@lowercase
def greet_l():
    ''' Just return a greeting string'''
    return 'HELLO !'

print(greet_l.__name__)
print(greet_l.__doc__)

"""


# decorators can work on functions 
# with arguments. In such case, positional
# and keyword arguments will be used to pass
# the argument
# Ex - 3
'''
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}()  '
              f'with {args}, {kwargs}')
        
        original_result= func(*args, **kwargs)
        
        print(f'TRACE: {func.__name__}()  '
              f'returned {args}, {kwargs}')
        
        return original_result
    
    return wrapper

@trace
def say(name,line):
    print('Inside :' )
    return f'{name}: {line}'

say('Madhab', 'How are you?')

'''
# Multiple decorators can be applied to 
# a function. In such scenario they will
# be applied from bottom up
# Ex - 2
'''
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'    
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

# This call actually translates to - 
# decorated_greet = strong(emphasis(greet))
print(greet())

'''

# Ex -1 - with decorator 
# - using decorator or pie @ operator instead of 
# - assigning the functions to decorator directly

"""
import time

def time_a_func(func):
    '''
    Output the time a functions takes to execute
    '''
    
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        
        print( "Time it took to run the function" + str((t2 - t1)) + "\n")
    
    return wrapper

@time_a_func
def my_func():
    num_list = []
    for i in range(0,10000):
        num_list.append(i)
    print("Sum of all the numbers : " + str(sum(num_list)))

#Calling my_func() will get called via time_a_func() decorator     
my_func()
"""


#real life usage of a decorator function
# - timing a function execution.
# - Ex - 1
"""
import time

def time_a_func(func):
    '''
    Output the time a functions takes to execute
    '''
    
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        
        print( "Time it took to run the function" + str((t2 - t1)) + "\n")
    
    return wrapper


def my_func():
    num_list = []
    for i in range(0,10000):
        num_list.append(i)
    print("Sum of all the numbers : " + str(sum(num_list)))
    
print(my_func)
# a decorator is meant to replace below code
my_func = time_a_func(my_func)
print(my_func)
my_func()

"""


# Why what decorator functions are required 
# for without using a decorator function

'''
def decorator(func):
    def wrapper():
        
        print('-'*10,'Before','-'*10)
        func()
        print('-'*10,'After','-'*10)
    return wrapper

def say_hello():
    print( 'Hello')

print(say_hello)

# the decorator function does what is mentioned below line 
say_hello = decorator(say_hello)
print(say_hello)
say_hello()

'''