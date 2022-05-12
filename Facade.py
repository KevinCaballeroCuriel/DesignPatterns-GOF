class ProcessingUnit:
    def process(self):
            print("Procesando...")
 
class DisplayUnit:
    def display(self):
            print("Mostrando...")
 
class Memory:
    def ioOperation(self):
            print("Leyendo y escribiendo en memoria...")
 
class Computer:
    def __init__(self):
        self.processingUnit = ProcessingUnit()
        self.displayUnit = DisplayUnit()
        self.memory = Memory()
 
    def bootUp(self):
        self.processingUnit.process()
        self.memory.ioOperation()
        self.displayUnit.display()
 
computer = Computer()
computer.bootUp()
