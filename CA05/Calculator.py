# -*- coding: utf-8 -*-

"""Calculator using lambda, mapreduce, filter, list comprehension, generator"""

#file no. 1 - defines the class Calculator and its methods/instances

class Calculator(object):
   
    def add(self,first,second):
        return map(lambda x,y: x+y, first, second)
    
    def subtract(self,first,second):
        return map(lambda x,y: x-y, first, second)
    
    def multiply(self,first,second):
        return map(lambda x,y: x*y, first, second)
    
    def divide(self,first,second):
        return map(lambda x,y: x/float(y) if y!=0 else 'Undefined', first, second)
    
    def exponent(self,first,second):
        return map(lambda x,y: x**y, first, second)
    
    def cube(self,first):
        return map(lambda x: x**3, first)
    
    def min(self,values):
        return reduce(lambda a,b: a if (a<b) else b, values)
    
    def square(self,first):
        return map(lambda x: x**2, first)
    
    def circle_area(self,first):
        from math import pi
        return map(lambda x: round(pi * x**2,2), first)
           
    def is_odd(self,values):
        return filter(lambda x: x%2==1, values)
    
    def pythagorean(self,n):
        for x in range(1,n):
            for y in range(x,n):
                for z in range(y,n):
                    if x**2 + y**2 == z**2:
                        yield (x,y,z)
    
    def comedian_generator(self):
        yield('Programming')
        yield('Is')
        yield('Amazing')
        yield("It's")
        yield('Like')
        yield('Magic')
    
    def euro_to_dollar(self,values):
        return [round((x*1.0868),2) for x in values]
        
    def euro_to_sterling(self):
        return lambda x: round(x*0.84,2)
    
    #update this function
    def sin(self,first):
        from math import sin
        from math import radians
        return sin(radians(first))

myCalc = Calculator()        

print myCalc.add([47,11,42,13],[47,11,42,13])    
print myCalc.subtract([47,11,42,13],[47,11,42,13])
print myCalc.divide([10,0,2],[5,20,0])
print myCalc.multiply([10,0.5,2],[5,20,0])
print myCalc.exponent([10,0.5,2],[5,20,0])
print myCalc.cube([1,5,10])
print myCalc.square([1,5,10])
print myCalc.circle_area([1,5,10])
print myCalc.is_odd([47,11,42,13,24,-47])

pyt = myCalc.pythagorean(30)
for x in pyt:
    print x,
    print sum(x)
    
funny = myCalc.comedian_generator()
for x in funny:
    print x,
print    

Euro = [39.2, 36.5, 37.3, 37.8]
dollar = myCalc.euro_to_dollar(Euro)
sterling = map(myCalc.euro_to_sterling(),dollar)
print dollar
print sterling
