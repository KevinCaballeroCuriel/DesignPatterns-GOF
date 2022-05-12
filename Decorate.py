def decorateMyFunction(originalFunction):
    def addAdditionalText():
        textFromOriginalFunction = originalFunction()
        return "<p>" + textFromOriginalFunction + "</p>"
    return addAdditionalText
 
@decorateMyFunction
def functionToBeDecorated():
    return "Hola a todos!"

print(functionToBeDecorated())   

