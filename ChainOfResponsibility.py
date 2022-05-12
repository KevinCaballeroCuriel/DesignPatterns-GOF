class AbstractHandler:
        def __init__(self, successor):
                self._successor = successor
        def handle(self, request):
                handled = self.processRequest(request)
                if not handled:
                        self._successor.handle(request)
        def processRequest(self, request):
                raise NotImplementedError
                ('¡Debe proporcionar implementación en subclase!')
 
class ConcreteHandlerOne(AbstractHandler):
        def processRequest(self, request):
                
                if 0 < request <= 10:
                        print("Esto es {} solicitud de manejo '{}'".format
                        (self.__class__.__name__, request))
                        return True
 
class ConcreteHandlerTwo(AbstractHandler):
        def processRequest(self, request):
                if 10 < request <= 20:
                        print("Esto es {} solicitud de manejo '{}'".format(self.__class__.__name__, request))
                        return True
 
class DefaultHandler(AbstractHandler):
        def processRequest(self, request):
                print("Esto es {} diciéndote esa solicitud '{}' no tiene manejador en este momento.".format(self.__class__.__name__, request))
                return True
 
class Client:
        def __init__(self):
                self.handler = ConcreteHandlerOne(
                        ConcreteHandlerTwo(DefaultHandler(None)))
        def delegate(self, requests):
                for request in requests:
                        self.handler.handle(request)
 
clientOne = Client()
 
requests = [6, 12, 24, 18]
 
clientOne.delegate(requests)
