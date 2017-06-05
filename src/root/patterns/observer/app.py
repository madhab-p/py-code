'''
Created on Apr 26, 2017
@description:
 This app is to test the observer pattern built
 using observerable and observer.
 
@author: pneela
'''
from src.root.patterns.observer.observer import Observer
from src.root.patterns.observer.observable import Observable

class AmericalStockExchange(Observer):
    def update(self, *args, **kwargs):
        # f - is f-string in pythin introduced in 3.6
        print(f'American stock market recived : {args} \n {kwargs}')

class LondonStockExchange(Observer):
    def update(self, *args, **kwargs):
        print(f'London stock market recived : {args} \n {kwargs}')
    

if __name__ == "__main__":    
    
    print('Start execution..' )
    observavle = Observable()
    ase_observer = AmericalStockExchange();
    observavle.register(ase_observer);
    
    lse_observer = LondonStockExchange();
    observavle.register(lse_observer);
    
    observavle.update_observers("Market Rally", something='Keep buying....')
    
    
    
        