# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:32:01 2017

@author: Colum
"""

class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''
    
    def setColour(self, value):
        self.__colour = value
        
    def setMake(self, value):
        self.__make = value
        
    def setMileage(self, value):
        self.__mileage = value
        
    def getColour(self):
        return self.__colour
    
    def getMake(self):
        return self.__make
    
    def getMileage(self):
        return self.__mileage
    
    def paint(self, value):
        print('Painting car ' + value)
        self.__colour = value
    
    def move(self, distance):
        print ('Moved ' + str(distance) + ' kms.')
        self.__mileage = self.__mileage + distance

#print myCar.__colour #cannot access it as it's private
    
class ElectricCar(Car):
    def __init__(self,numCells=1):
        #Car.__init__(self)
        self.__numberFuelCells = numCells
        
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
        
class PetrolCar(Car):
    def __init__(self,engineSizePetrol=1.2):
        self.engineSize = engineSizePetrol     

    def setEngineSize(self, value):
        self.engineSize = value
        
    def getEngineSize(self):
        return self.engineSize

class DieselCar(Car):
    def __init__(self,engineSizeDiesel=1.4):
        self.engineSize = engineSizeDiesel
        
    def setEngineSize(self, value):
        self.engineSize = value
        
    def getEngineSize(self):
        return self.engineSize

class HybridCar(ElectricCar):
    def __init__(self, numFuelCells, engineSizePetrol=1.2):
        ElectricCar.__init__(self,numFuelCells)
        self.engineSize = engineSizePetrol
    
    def setEngineSize(self, value):
        self.engineSize = value
        
    def getEngineSize(self):
        return self.engineSize
        
class Dealership(object):
    
    """Aungier Car Rental has a fleet of 40 cars, which consists of 20 petrol, 8 diesel, 
        4 electric and 8 hybrid cars. The store has just opened and all cars are currently 
        available to rent"""
    
    def __init__(self, days=1, unitCost=50):
        self.electric_cars = []
        self.petrol_cars = []
        self.hybrid_cars = []
        self.diesel_cars = []
        self.days = days
        self.__cost = unitCost
        self.value = 0
    
    def create_current_stock(self,stock=40):
        self.__stock = stock
        for i in range(int(self.__stock*0.1)):
           self.electric_cars.append(i)
        for i in range(int(self.__stock*0.5)):
            self.petrol_cars.append(i)
        for i in range(int(self.__stock*0.2)):
           self.diesel_cars.append(i)
        for i in range(int(self.__stock*0.2)):
            self.hybrid_cars.append(i)

    def stock_count(self):
        print 'petrol cars in stock: ' + str(len(self.petrol_cars))
        print 'electric cars in stock: ' + str(len(self.electric_cars))
        print 'hybrid cars in stock: ' + str(len(self.hybrid_cars))
        print 'diesel cars in stock: ' + str(len(self.diesel_cars))

    def set_car_rent(self, car_list, amount):
        if  amount > len(car_list):
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
            car_list.pop()
            total = total + 1
    
    def get_car_rent(self,car_list):
        return len(car_list)

    def set_car_return(self, car_list, amount):
        #if amount + len(car_list) > self.max_cars:
        if len(car_list) + amount > 20: # update this to capture different car inventory levels
            print "Error, too many cars returned"
            return
        total = 0
        while total < amount:
            car_list.append(amount)
            total = total + 1
    
    def get_car_return(self,car_list):
        return len(car_list)
            
    def set_rental_price(self,amount,days):
        '''Car rental cost is 50 euro per day as standard. Rentals for three or more days receive a 
        10% reduction in daily rate. Rentals for seven or more days receive a 20% reduction in daily rate.
        A maximum of 1 car can be rented per visit.'''
        #days = UserInputs.numinputs('Please enter no. of rental days: ')
        #need to multiply by no. of cars ordered
        #days = raw_input('Please specify number of rental days: ')
        if days < 3:
            self.value = amount * days * self.__cost   
        elif days >= 3 and days < 7:
            self.value = amount * (days * self.__cost)*0.9
        elif days >= 7:
            self.value = amount * (days *self.__cost)*0.8
        else:
            print 'Please enter a numeric value'
        print 'Invoice for the car rental is: {}'.format(self.value)
    
    def get_rental_price(self):
        return self.value
    
    def process_rental(self):
        while True:
            answer = raw_input('Enter 1 to rent or 2 to return: ')
            if answer == '1':
                answer = raw_input('Specify car type (P/D/E/H): ').lower()
                amount = int(raw_input('Specify amount: '))
                days = int(raw_input('Specify number of days required: '))
                if answer == 'p':
                    self.set_car_rent(self.petrol_cars, amount)
                elif answer == 'd':
                    self.set_car_rent(self.diesel_cars, amount)
                elif answer == 'h':
                    self.set_car_rent(self.hybrid_cars, amount)
                else:
                    self.set_car_rent(self.electric_cars, amount)
                self.set_rental_price(amount,days)
                
            elif answer == '2':
                answer = raw_input('Specify car type (P/D/E/H): ').lower()
                amount = int(raw_input('Specify amount: '))
                if answer == 'p':
                    self.set_car_return(self.petrol_cars, amount)
                elif answer == 'd':
                    self.set_car_return(self.diesel_cars, amount)
                elif answer == 'h':
                    self.set_car_return(self.hybrid_cars, amount)
                else:
                    self.set_car_return(self.electric_cars, amount)
            self.stock_count()