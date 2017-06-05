'''
Created on May 26, 2017

@author: pneela

This explain how to build iterative functions using 
- iterator
- generator
- generator expression
- getitem method
'''

#generator
def uc_gen(text):
    for char in text:
        yield char.upper()
        

#generator expression
def uc_genexp(text):
    return (char.upper() for char in text)        


#iterator Protocol

class uc_iter():
    def __init__(self,text):
        self.text = text
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
            
        self.index +=1
        return result
    
#getitem method of a class
class uc_getitem():
    def __init__(self,text):
        self.text = text
    
    def __getitem__(self,index):
        result = self.text[index].upper()
        return result;

for iterator in uc_gen, uc_genexp,uc_getitem,uc_iter:
    for ch in iterator('abcde'):
        print(ch,end=" ")
    print()
    