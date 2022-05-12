class Core:
        def __init__(self, name):
                self._observers = []
                self._name = name
                self._temp = 0
 
        def attach(self, observer):
                if observer not in self._observers:
                        self._observers.append(observer)
        def detach(self, observer):
                try:
                        self._observers.remove(observer)
                except ValueError:
                        print("La observadora ya no está en la lista de observadoras.")
        def notify(self):
                for observer in self._observers:
                        observer.update(self)
                 
        @property
        def temp(self):
                return self._temp
 
        @temp.setter
        def temp(self, temp):
                self._temp = temp
                self.notify()
                 
class FacultyMonitoringCore:
        def update(self, subject):
                if subject._temp > 350:
                    print(
                        "El Núcleo de Monitoreo Docente dice: {} tiene temperatura {}. Código Rojo!!!".format(subject._name, subject._temp))
                else:
                    print(
                        "El Núcleo de Monitoreo Docente dice: {} tiene temperatura {}. Todo está bajo control.".format(subject._name, subject._temp))
 
coreOne = Core("Nucleo 1")
 
facultyMonitoringCoreOne = FacultyMonitoringCore()
facultyMonitoringCoreTwo = FacultyMonitoringCore()

coreOne.attach(facultyMonitoringCoreOne)
coreOne.attach(facultyMonitoringCoreTwo)
 
coreOne.temp = 300
coreOne.temp = 360
