'''
Created on Apr 17, 2017

@author: pneela
'''
from sys import argv

print(len(argv))
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

data_from_input  = input('Enter data: ')
print(data_from_input)