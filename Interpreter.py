import re
class CamelCase(object):

    def __init__(self):
        self.SomeProperty = "Una propiedad"

    def SomeMethod(self, argument):
        print(argument)

class CamelCaseInterpreter(object):
    
    def __init__(self, old_class):
        super(CamelCaseInterpreter, self).__setattr__("__old_class", old_class)

    def __getattribute__(self, name):
        old_class = super(CamelCaseInterpreter, self).__getattribute__(
                                                        "__old_class")
        converter = super(CamelCaseInterpreter, self).__getattribute__(
                                                    "name_converter")
        return old_class.__getattribute__(converter(name))

    def __setattr__(self, name, value):
        old_class = super(CamelCaseInterpreter, self).__getattribute__(
                                                        "__old_class")
        converter = super(CamelCaseInterpreter, self).__getattribute__(
                                                        "name_converter")
        old_class.__setattr__(converter(name), value)

    def name_converter(self, name):
        new_name = name[0].upper()
        previous_underscore = new_name == "_"
        for char in name[1:]:
            if (char == "_"):
                previous_underscore = True
            else:
                if (previous_underscore):
                    new_name += char.upper()
                else:
                    new_name += char
                previous_underscore = False
        return new_name

if (__name__ == "__main__"):
    old_class = CamelCase()

    interpreted_class = CamelCaseInterpreter(old_class)
    print(interpreted_class.some_property)

    interpreted_class.some_property = "Propiedad recién configurada"
    print(interpreted_class.some_property)

    interpreted_class.some_method("Argumento de algún método")


