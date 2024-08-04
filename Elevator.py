import os

class Elevator:
    __destFloor = 0
    __currFloor = 0
    __doorState = "" # OPEN / CLOSED

    def __init__(self):
        self.__destFloor = 1
        self.__currFloor = 1
        doorState = "CLOSED"

    def __del__(self):
        pass

    def setFloor(self, f):
        self.__currFloor = f

    def getFloor(self):
        return self.__currFloor

    def moveFloor(self, callingFloor):
        tmpFloor = self.__currFloor
        if callingFloor > self.__currFloor:
            while tmpFloor < callingFloor:
                print "UP", tmpFloor
                os.system("sleep 1s")
                tmpFloor+=1
            self.__currFloor = callingFloor
            print "Now the elevator has reached Floor %d." % callingFloor
        elif callingFloor < self.__currFloor:
            while tmpFloor > callingFloor:
                print "DOWN", tmpFloor
                os.system("sleep 1s")
                tmpFloor-=1
            self.__currFloor = callingFloor
            print "Now the elevator has reached Floor %d." % callingFloor
        else:
            print "the elevator is already on the floor."

    def openDoor(self):
        doorState = "OPEN"
        print "The door has opened."

    def closeDoor(self):
        doorState = "CLOSED"
        print "The door has closed."

# __main__
elev = Elevator()
print elev.getFloor()
elev.moveFloor(4)
elev.moveFloor(10)
elev.moveFloor(1)
