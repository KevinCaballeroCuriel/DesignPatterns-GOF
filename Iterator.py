class CountTo:
    def __init__(self, upperBound):
        self.upperBound = upperBound
        self.numbersInSpanish = ["Uno", "Dos", "Tres", "Cuatro", "Cinco", 'Seis', 'Siete', 'Ocho', 'Nueve']
        self.numbersInSpanish = self.numbersInSpanish[:upperBound]      
        self.index = 0       
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.numbersInSpanish[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
 
number = int(input("Dame un numero del 1 al 9: "))
countToNumber = CountTo(number)

for i in range(1,number + 1):
    print(next(countToNumber))

