class Car:
    __name=""
    __speed=0

    def setName(self, name):
        self.__name = name
    def setSpeed(self, speed):
        self.__speed = speed
    def setCar(self, name, speed):
        self.setName(name)
        self.setSpeed(speed)
    def getName(self):
        return self.__name
    def getSpeed(self):
        return self.__speed
    def speedUp(self, degree):
        if(self.__speed + degree >= 200):
            print "You can't go faster than 200km/h."
            return 1
        else:
            print "accelerating to", str(self.__speed + degree)+"km/h."
            self.__speed += degree
            return 0
    def speedDown(self, degree):
        if(self.__speed - degree <= 0):
            print "decelerating to", "0"+"km/h."
            self.__speed = 0
            return 0
        else:
            print "decelerating to", str(self.__speed - degree)+"km/h."
            self.__speed -= degree
            return 0
    def showCar(self):
        print " **Car Name:", self.__name
        print " **Speed:", str(self.__speed)+"km/h"

mycar = Car()

mycar.setName("Sonata")
mycar.setSpeed("100")
mycar.showCar()

mycar.setCar("Santa Fe", 25)
mycar.showCar()

mycar.speedUp(76)
mycar.showCar()

mycar.speedDown(20)
mycar.showCar()

mycar.speedUp(230)
mycar.showCar()
