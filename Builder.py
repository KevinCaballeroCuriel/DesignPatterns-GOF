class Car():
    def __init__(self):
        self.engine = None
        self.tyres = None
        self.speedometer = None
    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.tyres, self.speedometer)      
 
class AbstractBuilder():
    def __init__(self):
        self.car = None
    def createNewCar(self):
        self.car = Car()
 
class ConcreteBuilder(AbstractBuilder):
    def addEngine(self):
        self.car.engine = "Motor de 4 Cilindros"
    def addTyres(self):
        self.car.tyres = "Llantas MRF"
    def addSpeedometer(self):
        self.car.speedometer = "0-160 Millas"
 
class Director():
    def __init__(self, builder):
        self._builder = builder
    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addEngine()
        self._builder.addTyres()
        self._builder.addSpeedometer()
    def getCar(self):
        return self._builder.car
 
concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
 
director.constructCar()
carOne = director.getCar()
print("Detalles del carro:", carOne)

