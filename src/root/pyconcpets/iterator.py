'''
Created on May 26, 2017

@author: pneela
'''

class yrange:
    def __init__(self,n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        '''Iterators return self but Iterables return iterators'''
        
        #below line enable the iterator to be used again and again
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


if __name__ == "__main__":
    print('In the main ....')
    y = yrange(10)
    for i in y:
        print(i)
    
    # below two line will get result if 
    # __iter__() returns a iterator that reset the self.i value to start again
    # NOTE: for look calls the __iter__() to get the iterator 
    # to fetch the results by calling __next__(), so by resetting self.i
    # iterator is ready for reuse
    
    li = [i for i in y]
    print(li)