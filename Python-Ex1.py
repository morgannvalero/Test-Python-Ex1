# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 08:56:25 2020

@author: Morgann
"""
## Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

## Method 1 using math library
import math
class Circle1:
    def __init__(self, r):
        perimeter= 2*math.pi*r
        area = math.pi*r**2
        self.result = "perimeter = " + str(perimeter) + " m and area = " + str(area) +" m^2"
        
## test saying that input is in meter  
test = Circle1(1)
print(test.result)

## Method 2 using scipy library
import scipy
class Circle2:
    def __init__(self, r):
        perimeter= 2*scipy.pi*r
        area = scipy.pi*r**2
        self.result = "perimeter = " + str(perimeter) + " m and area = " + str(area) +" m^2"
        
## test saying that input is in meter  
test2 = Circle2(1)
print(test2.result)

## Results are the same (hopefully)

