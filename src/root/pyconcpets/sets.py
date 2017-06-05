'''
Created on Apr 11, 2017

@author: pneela
'''


a_set = {'a','11',1,23.55,-1,'This is an element'}
a_list = ['a','11',1,23.55,-1,'This is an element']
a_dict = {'a' :1,'b':2}


print(type(a_set))
print(type(a_list))
print(type(a_dict))

a_set = set(('a','11',1,23.55,-1,'This is an element'))
a_list = list(('a','11',1,23.55,-1,'This is an element'))
a_dict = dict({'a':1,'b':2,'there is one':1})



print(type(a_set))
print(type(a_list))
print(type(a_dict))