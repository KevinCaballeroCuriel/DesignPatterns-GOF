# Different classes denoting different types of objects having a common characteristic: Knight, Rook & Bishop
class Knight:
    #One of many classes having a common characteristic
    def directionOfMovement(self):
        return "Ni horizontal ni vertical."
    def stepsInMovement(self):
        return "Dos y medio"
    def __str__(self):
        return "Caballero"
 
class Rook:
    #One of many classes having a common characteristic'''
    def directionOfMovement(self):
        return "Horizontal o verticalmente."
    def stepsInMovement(self):
        return "Tantas como 7."
    def __str__(self):
        return "Fumar"
 
class Bishop:
    #One of many classes having a common characteristic'''
    def directionOfMovement(self):
        return "Diagonalmente."
    def stepsInMovement(self):
        return "Tantas como 7."
    def __str__(self):
        return "Alfil"
 
# Concrete Factories having getter methods to return objects of above classes: KnightFactory, RookFactory & BishopFactory
class KnightFactory:
    #Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Knight()
 
class RookFactory:
    #Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Rook()
 
class BishopFactory:
    #Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Bishop()
 
# Abstract Factory which takes a concrete factory object as input, obtains the object from the factory, and provides a method to expose details of the object: Piece Factory
class PieceFactory:
    #An abstract factory which takes a concrete factory object as input, obtains the object from the factory, and provides a method to expose details of the object. '''
    def __init__(self, pieceFactory):
        self._pieceFactory = pieceFactory
         
    def detailsOfChosenPiece(self):
        #utility method to display details of object returned by the abstract factory'''
        chosenPiece = self._pieceFactory.getPiece()
        print("Pieza elegida:", chosenPiece)
        print("Dirección de la pieza elegida:", chosenPiece.directionOfMovement())
        print("Número de pasos que puede mover la pieza elegida:", chosenPiece.stepsInMovement())
 
objectOfConcreteFactory = KnightFactory()
objectOfAbstractFactory = PieceFactory(objectOfConcreteFactory)
objectOfAbstractFactory.detailsOfChosenPiece()

