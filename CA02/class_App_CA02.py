
from class_car_CA02 import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, Dealership

import random 

red_car = Car()
print 'Colour ' + red_car.getColour()
print 'Mileage ' + str(red_car.getMileage())
print 'Make ' + red_car.getMake()

red_car.setMake('Ferrari')
print 'Make ' + red_car.getMake()
print 'Colour ' + red_car.getColour()
print ('Car moved' + str(red_car.move(15)) + 'kms')
print 'Mileage ' + str(red_car.getMileage())
print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize

marque = ['Ford','Toyota','BMW','Fiat','Nissan','Hyundai','Renault']
colour = ["Red","Green","Black","Grey","Silver"]
mileage = [50,100,250,500,1000,1500]
move = [100,200,300,400,500,750,900]
engineSizePetrol = [1.0, 1.2, 1.4, 1.6, 2.0]
engineSizeDiesel = [1.4, 1.6, 2.0, 2.4, 3.0]
numCells = [1,2]

p_car1 = PetrolCar()
p_car1.setColour(random.choice(colour))
p_car1.setMileage(random.choice(mileage))
p_car1.setEngineSize(random.choice(engineSizePetrol))

print 'Colour: ' + p_car1.getColour()
print 'Mileage: ' + str(p_car1.getMileage())
print 'Engine Size: ' + str(p_car1.getEngineSize())
p_car1.move(random.choice(move))

dealership = Dealership()

dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('Do you wish to continue? y/n: ')

