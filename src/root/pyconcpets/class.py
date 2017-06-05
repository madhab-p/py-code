'''
Created on Apr 13, 2017

@author: pneela
'''

class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        ''' Check if sum of angles is 180 degree'''
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False         

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        ''' No need to pass angles since it is known'''
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
        
        
        
my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


my_eq_triangle = Equilateral()
print(my_eq_triangle.check_angles())