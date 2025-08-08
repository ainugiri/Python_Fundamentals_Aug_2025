# OOP - class and object 
# Class is a blue print
# object - instance of class, realtime entity, 

class Car:
    # set of property, set of function
    # brand, color, fuelType
    # Start, gearUp, gearDown, brake, accel, stop
    def __init__(self, brand,color, fuelType):
        self.brand = brand
        self.color = color
        self.fuelType = fuelType
    def start(self):
        print('Start the car')
    def gearUp(self):
        print('increase power to speedup')
    def gearDown(self):
        print('decrease power to speed down')
    def brake(self):
        print('decrease speed to 0 mph')
    def accel(self):
        print('increase speed by 10')
    def stop(self):
        print('Engine stoped')


mycar1 = Car('Ford','Gold','Petrol')
print(mycar1.brand)
mycar1.start()

mycar2 = Car('BMW','White', 'EV')
print(mycar2.brand)
mycar2.start()
mycar2.gearUp()
mycar2.accel()
mycar2.brake()
mycar2.stop()

# Template -> realtime entity 
# Class - Object
# Car - mycar1, mycar2

