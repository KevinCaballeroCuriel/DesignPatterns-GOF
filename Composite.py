class ChildElement:
        def __init__(self, *args):
                self.name = args[0]
        def printDetails(self):
                print("\t", end = "")
                print(self.name)
 
class CompositeElement:
        def __init__(self, *args):
                self.name = args[0]
                self.children = []
        def appendChild(self, child):
                self.children.append(child)
        def removeChild(self, child):
                self.children.remove(child)
        def printDetails(self):
                print(self.name)
                for child in self.children:
                        print("\t", end = "")
                        child.printDetails()

topLevelMenu = CompositeElement("Menú Top")
subMenuItem1 = CompositeElement("SubMenú1 Articulo1")
subMenuItem2 = CompositeElement("SubMenú1 Articulo2")
subMenuItem11 = ChildElement("SubMenú2 Articulo1.1")
subMenuItem12 = ChildElement("SubMenú2 Articulo1.2")
subMenuItem1.appendChild(subMenuItem11)
subMenuItem1.appendChild(subMenuItem12)
topLevelMenu.appendChild(subMenuItem1)
topLevelMenu.appendChild(subMenuItem2)
topLevelMenu.printDetails()
