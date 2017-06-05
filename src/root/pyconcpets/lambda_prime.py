'''
Created on Apr 13, 2017

@author: pneela
'''
''' Sieve of Eratosthenes '''

nums = range(2, 50) 
for i in range(2, 8): 
    nums = list(filter(lambda x: x == i or x % i, nums))
    print(nums)
 
print(list(nums))