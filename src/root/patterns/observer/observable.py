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


class Observable(object):
    def __init__(self):
        self.observers = []
    
    def register(self,observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def unregister(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
        
    def update_observers(self,*args,**kwargs):
        for observer in self.observers:
            observer.update(*args,**kwargs)
