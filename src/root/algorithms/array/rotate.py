'''
Created on Apr 19, 2017

@author: pneela


Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.

'''
from _ast import Num

'''
# using array slicing - arr[start:end:stop]
# - :end value represents the first value that is not in the selected slice."
# zero width slice - arr[0:0]
 
'''
def rotate(arr,k):
    n = len(arr)
    arr[0:0] = arr[n-k:]
    #remove the already roatated numbers
    arr[n:] = []
    return arr

def rotate_by_swap(arr,k):
    n = len(arr)
    k = n % k
    swap(arr,0,n-k-1)
    swap(arr,n-k,n-1)
    swap(arr,0,n-1) 

def swap(arr,a,b):
    while a < b :
        arr[a],arr[b] = arr[b],arr[a]
        a += 1
        b -= 1


arr = [1,2,3,4,5,6,7]
print(arr)
rotate_by_swap(arr, 3)
print(arr)