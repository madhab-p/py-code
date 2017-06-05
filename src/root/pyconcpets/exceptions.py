'''
Created on Apr 14, 2017

@author: pneela
'''

try:
    raise Exception('Spam','Egg')
except Exception as instance:
    print(type(instance))
    print(instance)
    print(type(instance.args))
    print(instance.args)
    
    x,y = instance.args
    print(x,y)


'''
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D exception')
    except C:
        print('C exception')
    except B:
        print('B excpetion')
        
    
while True:
    try: 
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print("Opps.. Try again")
    

try:
    print('Try:This is a risky operations')
    #tex2t.txt file doesn't exist
    raise(IOError('File doesnot exist'))
    open('tex2t.txt', 'r')
except IOError as err:
    print('Except: This is due to IO issues ' , err)
else:
    print('Else: No exception raised')    
finally:
    print('Finally: This is executed always - exeception or not')
'''