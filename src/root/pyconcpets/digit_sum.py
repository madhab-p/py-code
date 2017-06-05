'''
Created on Apr 11, 2017

@author: pneela
'''
def digit_sum(n):
    ''' Getting all the digits of a number using % & //'''
    if type(n) != int:
        print('Non Integer found')
        return False
    
    sum_n = 0
    while n > 0:
        sum_n += n % 10
        n = n // 10
    return sum_n

print(digit_sum('ss'))
