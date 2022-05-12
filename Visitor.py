class Crop:
    def accept(self, visitor):
        visitor.visit(self)
    def sow(self, visitor):
        print(self, "Sembrada por", visitor)
    def irrigate(self, visitor):
        print(self, "Regado por", visitor)
    def harvest(self, visitor):
        print(self, "Cosechado por", visitor)
    def __str__(self):
        return self.__class__.__name__
class Trigo(Crop): pass
class Maiz(Crop): pass
class Tomate(Crop): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__
 
class GardenerOne(Visitor):
    def visit(self, crop):
        crop.sow(self)
 
class GardenerTwo(Visitor):
    def visit(self, crop):
        crop.irrigate(self)
 
class GardenerThree(Visitor):
    def visit(self, crop):
        crop.harvest(self)
 
wheatPatch = Trigo()
cornPatch = Maiz()
tomatoPatch = Tomate()
 
gardenerOne = GardenerOne()
gardenerTwo = GardenerTwo()
gardenerThree = GardenerThree()
 
wheatPatch.accept(gardenerOne)
wheatPatch.accept(gardenerTwo)
wheatPatch.accept(gardenerThree)
 
cornPatch.accept(gardenerOne)
cornPatch.accept(gardenerTwo)
cornPatch.accept(gardenerThree)
 
tomatoPatch.accept(gardenerOne)
tomatoPatch.accept(gardenerTwo)
tomatoPatch.accept(gardenerThree)
