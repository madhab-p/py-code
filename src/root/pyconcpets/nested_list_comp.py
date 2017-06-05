'''
Created on May 19, 2017

@author: pneela
'''

'''
Transform a 3X4 matrix 

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]
     ]

to 

[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

using various techniques esp. nested list comp
'''

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]
     ]

print(matrix)

rev_matrix = [[row[i] for row in matrix] for i in range(4) ]
print('Using nested list comp..')
print(rev_matrix)

'''The same can be written as follows'''
rev_matrix = []
for i in range(4):
    rev_matrix_row = [] 
    for row in matrix:
        rev_matrix_row.append(row[i])
    rev_matrix.append(rev_matrix_row)
    
print('Using multiple loops..')
print(rev_matrix)

print('using zip inbuilt function..')
rev_matrix = [list(tu) for tu in zip(*matrix)]
print(rev_matrix)

