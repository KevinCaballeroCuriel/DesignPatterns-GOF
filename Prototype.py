import copy
 
class Car:
        def __init__(self):
                self.engine = "3200cc de capacidad del motor"
                self.color = "Azul"
                self.seats = "5 asientos"
        def __str__(self):
                return  '{} | {} | {}'. format(self.engine, self.color, self.seats)
 
class Prototype:
        def __init__(self):
                self._toBeClonedObjects = {}
        def registerObject(self, name, obj):
                self._toBeClonedObjects[name] = obj
        def unregisterObject(self, name):
                del self._toBeClonedObjects[name]
        def clone(self, name, **kwargs):
                clonedObject = copy.deepcopy(self._toBeClonedObjects.get(name))
                clonedObject.__dict__.update(kwargs)
                return clonedObject
 
defaultCar = Car()                                                      
prototype = Prototype()
prototype.registerObject('carroEjemplo', defaultCar)            
 
carOne = prototype.clone('carroEjemplo')                          
print("Detalles del carro 1:", carOne)                             
 
carTwo = prototype.clone('carroEjemplo', color = "Negro")  
print("Detalles del carro 2:", carTwo)