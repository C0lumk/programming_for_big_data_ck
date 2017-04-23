# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:12:56 2017

@author: Colum
"""

import unittest

from class_car_CA02 import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, Dealership

class CarTest(unittest.TestCase):
    
    def setUp(self):
        self.myCar = Car()
    
    def testCarEngineSize(self):
        self.myCar.engineSize = '2.0tdi'
        self.assertEqual('2.0tdi', self.myCar.engineSize)
    
    def testCarMake(self):
        self.myCar.setMake('Ferrari')
        self.assertEqual('Ferrari', self.myCar.getMake())
    
    def testCarMove(self):
        self.myCar.setMileage(10)
        self.myCar.move(20)
        self.assertEqual(30, self.myCar.getMileage())
        
    def testCarPaint(self):
        self.myCar.setColour('Red')
        self.assertEqual('Red', self.myCar.getColour())
        self.myCar.paint('Yellow')
        self.assertEqual('Yellow', self.myCar.getColour())
 
class ElectricCarTest(unittest.TestCase):
    
    def testCarNumberFuelCells(self):
        myCar = ElectricCar()
        self.assertEqual(1, myCar.getNumberFuelCells())
        myCar.setNumberFuelCells(2)
        self.assertEqual(2, myCar.getNumberFuelCells())    

class PetrolCarTest(unittest.TestCase):
    # exact same test for diesel cars
    def testEngineSize(self):
        myCar = PetrolCar()
        self.assertEqual(1.2, myCar.getEngineSize())
        myCar.setEngineSize(1.8)
        self.assertEqual(1.8, myCar.getEngineSize())

class HybridCarTest(unittest.TestCase):

    def testCarNumberFuelCells(self):
        myCar = HybridCar(PetrolCar)
        self.assertEqual(1.2, myCar.getEngineSize())
        myCar.setNumberFuelCells(4)
        self.assertEqual(4, myCar.getNumberFuelCells())
        
class DealershipTest(unittest.TestCase):
    
    def setUp(self):
        self.myCar = Dealership()
        
    def testRentalPrice(self):
        self.myCar.set_rental_price(2,1)
        self.assertEqual(100, self.myCar.get_rental_price())
        self.myCar.set_rental_price('Please enter a numeric value',1)
    
    def testRent(self):
        self.petrol_cars = []
        for i in range(20):
           self.petrol_cars.append(i)
        self.myCar.set_car_rent(self.petrol_cars,3)
        self.assertEqual(17,self.myCar.get_car_rent(self.petrol_cars))
    
    def testReturn(self):
        self.petrol_cars = []
        for i in range(20):
           self.petrol_cars.append(i)
        self.myCar.set_car_rent(self.petrol_cars,3)
        self.myCar.set_car_return(self.petrol_cars,2)
        self.assertEqual(19,self.myCar.get_car_return(self.petrol_cars))
    
if __name__ == '__main__':
    unittest.main()