# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:16:23 2017

@author: Colum
"""

#file no. 1 - defines the class Calculator and its methods/instances

class Calculator(object):
    
    def add(self, first, second):
        return first + second
    
    def subtract(self,first,second):
        return first - second
    
    def multiply(self,first,second):
        return first * second
    
    def divide(self,first,second):
        if first == 0:
            return 'undefined'
        elif second == 0:
            return 'undefined'
        return first / float(second)
    
    def exponent(self,first,second):
        return first ** second
    
    def cube(self,first):
        return first ** 3
    
    def square(self,first):
        return first ** 2
    
    def exponential(self,first):
        from math import exp
        return round(exp(first),2)
    
    def rectangleperimeter(self,first,second):
        return (first + second) * 2
    
    def pythagoras(self,first,second):
        from math import sqrt
        return round(sqrt(first ** 2 + second ** 2),2)
    
    def sin(self,first):
        from math import sin
        from math import radians
        return sin(radians(first))
    
    
    
