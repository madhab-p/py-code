''' 
flatten the array

Given an array that may contain nested arrays,
give a single resultant array.
'''

# default argument to a function
def list_flatten(l,a=None):
    # condtional if-else expression
    a = list(a) if isinstance(a, (list, tuple)) else []
        
    for i in l:
        if isinstance(i, (list, tuple)):
            #print('Reccurung i',i)
            a = list_flatten(i, a)
        else:
            #print(a)
            a.append(i)
    #print('a -->' ,a )
    return a


arr = [2, 1, [3, [4, 5], 6], 7, [8]]
print(list_flatten(arr))