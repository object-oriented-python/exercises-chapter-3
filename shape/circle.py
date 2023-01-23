import math
from math import sqrt

class Circle :

    def __init__(self, c, r):
        self.centre = c
        self.radius = r
    
    def __contains__(self,other):
        l = math.sqrt((other[0]-self.centre[0])**2 + (other[1]-self.centre[1])**2)
        if l < self.radius :
            return True
        else:
            return False