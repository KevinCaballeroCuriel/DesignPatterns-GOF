from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Trancisión a {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA encargandose de la solicitud 1.")
        print("ConcreteStateA quiere cambiar el estado del contexto.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA encargandose de la solicitud 2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB encargandose de la solicitud 1.")

    def handle2(self) -> None:
        print("ConcreteStateB encargandose de la solicitud 2.")
        print("ConcreteStateB quiere cambiar el estado del contexto.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()