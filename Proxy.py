class Car:
    def driveCar(self):
        print("El conductor puede seguir conduciendo el carro....")
 
class CarProxy:
    def __init__(self): 
        self.ageOfDriver = 15
        self.car = None
 
    def driveCar(self):
        print("Proxy en accion. Verificando edad del conductor...")
        if self.ageOfDriver >= 18:
            self.car = Car()
            self.car.driveCar()
        else:
            print("El conductor es menor de edad. No puede conducir el carro.")
 
carProxy = CarProxy()
carProxy.driveCar()
 
carProxy.ageOfDriver = int(input("Dime tu edad: "))
carProxy.driveCar()

