'''
Created on Apr 19, 2017

## find missing ranges between low and high in the given array.
# ex) [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]

@author: pneela
'''

def missing_ranges(nums,low,high):
    res = []
    start = low
    for num in nums:
        if num < start:
            continue
        if num == start:
            continue
        res.append(get_range(start, num-1))
        start = num +1
    if start <= high:
        res.append(get_range(start , high))
    return res

    
    

def get_range(start, end):
    if start == end :
        return str(start)
    else:
        return str(start) + ' -> ' + str(end)
    

nums = [2,5,7,8,9,10,15,17]

print(missing_ranges(nums, 4, 20))