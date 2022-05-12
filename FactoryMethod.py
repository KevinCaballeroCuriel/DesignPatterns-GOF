# Different classes denoting different types of objects having a common characteristic: Knight, Rook & Bishop
class Rook:
    '''A simple Rook class'''
    def move(self):
        return "Muevo cualquier cantidad de espacios, pero solo horizontal o verticalmente."
 
class Knight:
    '''A simple Knight class'''
    def move(self):
        return "Muevo 2 espacios y medio."
 
class Bishop:
    '''A simple Bishop class'''
    def move(self):
        return "Muevo cualquier cantidad de espacios en diagonal."
 
# A Factory Method that returns the object based on an input.
def makeChessPiece(piece):
    '''Factory method that takes a string and returns an object based on it.'''
    pieces = {"Caballo": Knight(), "Alfil": Bishop(), "Torre": Rook()}
    return pieces[piece]
 
class ChessPieceFactory:
    def createChessPiece(self, inputString):
        createdPiece = makeChessPiece(inputString)
        return createdPiece   
 
chessPieceFactory = ChessPieceFactory()
 
pieceOne = chessPieceFactory.createChessPiece('Caballo')
print("Caballo:", pieceOne.move())
 
pieceTwo = chessPieceFactory.createChessPiece('Alfil')
print("Alfil:", pieceTwo.move())
 
pieceThree = chessPieceFactory.createChessPiece('Torre')
print("Torre:", pieceThree.move())
 
