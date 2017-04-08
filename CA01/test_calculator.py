# -*- coding: utf-8 -*-

#file no. 4 - test file to check if each method is valid

from Calculator import Calculator
import unittest

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
        
    # test to see 2+2=4, 5+3=8, 4+0=4
    def testAdd(self):
        self.assertEqual(self.calc.add(2,2), 4)
        self.assertEqual(self.calc.add(5,3), 8)
        self.assertEqual(self.calc.add(4,0), 4)
    
    # test 2-2=0, 5-3=2, 4-0=0
    def testSubtract(self):
        self.assertEqual(self.calc.subtract(2,2), 0)
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(4,0), 4)
    
     # test 2*2=4, 5*3=15, 4*0=0, 3*-4=-12
    def testMultiply(self):
        self.assertEqual(self.calc.multiply(2,2), 4)
        self.assertEqual(self.calc.multiply(5,3), 15)
        self.assertEqual(self.calc.multiply(4,0), 0)
        self.assertEqual(self.calc.multiply(3,-4), -12)
        
    # test 2/2=1, 5/3=1, 5/2.5=2 12/-3=-4, 4/0=undefined
    def testDivide(self):
        self.assertEqual(self.calc.divide(2,2), 1)
        self.assertEqual(self.calc.divide(5,2), 2.5)
        self.assertEqual(self.calc.divide(5,2.5), 2)
        self.assertEqual(self.calc.divide(12,-3), -4)
        self.assertEqual(self.calc.divide(0,2), 'undefined')
        self.assertEqual(self.calc.divide(4,0), 'undefined')
    
    # test 2**2=4, 5**3=125, 5**0=1 0**3=0
    def testExponent(self):
        self.assertEqual(self.calc.exponent(2,2), 4)
        self.assertEqual(self.calc.exponent(5,3), 125)
        self.assertEqual(self.calc.exponent(5,0), 1)
        self.assertEqual(self.calc.exponent(0,3), 0)
        
    # test 2^3=8, 4^3=64, 0^3=0, -3^3=-27
    def testCube(self):
        self.assertEqual(self.calc.cube(2), 8)
        self.assertEqual(self.calc.cube(4), 64)
        self.assertEqual(self.calc.cube(0), 0)
        self.assertEqual(self.calc.cube(-3), -27)
        
    #  test 2^2=4, 4^2=16, 0^2=0, -3^2=9
    def testSquare(self):
        self.assertEqual(self.calc.square(2), 4)
        self.assertEqual(self.calc.square(4), 16)
        self.assertEqual(self.calc.square(0), 0)
        self.assertEqual(self.calc.square(-3), 9)
        
    # test exp(3)=20.085, exp(0)=1, exp(-2)=0.135, exp(1.5)=4.482
    def testExponential(self):
        self.assertEqual(self.calc.exponential(3), 20.09)
        self.assertEqual(self.calc.exponential(0), 1)
        self.assertEqual(self.calc.exponential(-2), 0.14)
        self.assertEqual(self.calc.exponential(1.5), 4.48)
        
    # test perimeter(3,2)=10, perimeter(1.5,10)=23, perimeter(3.5,7.5)=22
    def testRectanglePerimeter(self):
        self.assertEqual(self.calc.rectangleperimeter(3,2), 10)
        self.assertEqual(self.calc.rectangleperimeter(1.5,10), 23)
        self.assertEqual(self.calc.rectangleperimeter(3.5,7.5), 22)
    
    # test Pythagoras hypothenuse: (2,2)=2.83, (10,10)=14.14, (2.5,2.5)=3.54
    def testPythagoras(self):
        self.assertEqual(self.calc.pythagoras(2,2), 2.83)
        self.assertEqual(self.calc.pythagoras(10,10), 14.14)
        self.assertEqual(self.calc.pythagoras(2.5,2.5), 3.54)
        
    # test Sine: sin(90)=1, sin(0)=0,
    def testSine(self):
        self.assertEqual(self.calc.sin(90), 1)
        self.assertEqual(self.calc.sin(0), 0)
        
if __name__ == '__main__': # if this is run from the command line, then envoke. if it isn't, don't do anything
    unittest.main()
