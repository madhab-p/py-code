'''
Created on Apr 17, 2017

@author: pneela
'''

from sys import argv

# get the script name and filename from command line 
script,filename = argv

#open a file with read mode
txt = open(filename,'r')


print('Here is ur file %r' % filename)

## read the file content and print to the o/p
print(txt.read())

txt.close()