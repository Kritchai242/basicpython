class Car:
    # propertys
    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0
    # constructor

    def __init__(self, color, brand, maxspeed, number_of_wheel, number_of_seats):
        self.color = color
        self.brand = brand
        self.number_of_wheels = number_of_wheel
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    # Create method set color
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setmaxspeed(self, x):
        self.maxspeed = x

    def printdata(self):
        print("Color", self.color)
        print("Brand", self.brand)
        print("Max speed", self.maxspeed)
        #print("Number Seats:", self.brand)
        #print("Number Wheels:", self.maxspeed)
    # deconstructor

    def __del__(self):
        print
