# object and class

# Blue Honda Car

# maker, Color

# Template : Car : maker , color : Class

# object from a class

class Car:

    # self is the object that got created

    # by default gets executed

    # constructor   ###it is constructing an object

    def __init__(self, maker, color, topspeed):

        self.maker = maker

        self.color = color

        self.topspeed = topspeed

    def carQuality(self):

        if (self.topspeed > 100):

            print(" Its a high speed car")

        else:

            print(" Its not so hgh speed")

 

# invoke an object

# creating an object called car1

car1 = Car("Honda", "Blue", 50)

car1.carQuality()

print(car1.maker)

car2 = Car("BMW", "Red", 150)

car2.carQuality()