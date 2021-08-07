

class ParkingSystem:

    def __init__(self, big, medium, small):
        self.lista=[big,medium,small]

    def addCar(self, carType):
        if self.lista[carType-1]>=1:
            self.lista[carType-1]=self.lista[carType-1]-1
            return True
        else:
            return False