'''
Created on Apr 13, 2017

@author: pneela
'''

class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d %d %d)" %(self.x,self.y,self.z)
        
my_point = Point3D(12,33,22)
print(my_point)    