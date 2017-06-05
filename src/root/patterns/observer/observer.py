'''
Created on Apr 26, 2017

@description:  
    A software design pattern in which an object, 
    called the subject, maintains a list of its dependents, 
    called observers, and notifies them automatically of 
    any state changes, usually by calling one of their methods. 
    It is mainly used to implement distributed event handling systems.

@author: pneela
'''

from abc import ABCMeta, abstractmethod

class Observer(object,metaclass=ABCMeta):
    
    @abstractmethod
    def update(self,*args, **kwargs):
        # if this function is not implemented 
        # then raise exception
        raise Exception
        pass