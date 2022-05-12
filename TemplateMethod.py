from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass dice: Estoy haciendo gran parte del trabajo")

    def base_operation2(self) -> None:
        print("AbstractClass dice: Pero dejo que las subclases realicen algunas operaciones")

    def base_operation3(self) -> None:
        print("AbstractClass dice: Pero estoy haciendo gran parte del trabajo de todas formas")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 dice: Operación 1 Implementada")

    def required_operations2(self) -> None:
        print("ConcreteClass1 dice: Operación 2 Implementada")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 dice: Operación 1 Implementada")

    def required_operations2(self) -> None:
        print("ConcreteClass2 dice: Operación 2 Implementada")

    def hook1(self) -> None:
        print("ConcreteClass2 dice: Operación Anulada")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()

if __name__ == "__main__":
    print("El mismo código de cliente puede funcionar con diferentes subclases: subclase 1")
    client_code(ConcreteClass1())
    print("")

    print("El mismo código de cliente puede funcionar con diferentes subclases: subclase 2")
    client_code(ConcreteClass2())

