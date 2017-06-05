'''
Created on May 26, 2017

@author: pneela
'''

class rev_iterator:
    def __init__(self,l):
        self.l = l
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if len(self.l) == 0:
            raise StopIteration
        else:
            return self.l.pop()
        
if __name__ == '__main__':
    it = rev_iterator([1, 2, 3, 4])

    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())