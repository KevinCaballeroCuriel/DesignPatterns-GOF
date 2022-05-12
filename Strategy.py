import sys
import types

if sys.version_info[0] > 2:                                                                              
    createBoundMethod = types.MethodType
         
class Strategy:
    def __init__(self, strategyName = 'Estrategia por defecto', replacementFunction=None):
        self.name = strategyName
        if replacementFunction:
            self.execute = createBoundMethod(replacementFunction, self)       
 
    def execute(self):
        print("Ejecutando {}...".format(self.name))
 
def strategyOne(self):
    print("Ejecutando {}...".format(self.name))
  
def strategyTwo(self):
    print("Ejecutando {}...".format(self.name))
 
     
defaultStrategy = Strategy()
 
strategyONE = Strategy('Estrategia Uno', strategyOne)
 
strategyTWO = Strategy('Estrategia Dos', strategyTwo)
 
defaultStrategy.execute()
strategyONE.execute()
strategyTWO.execute()