from pure_interface import Interface, abstractmethod


class ITraining(Interface):
    @property
    @abstractmethod
    def start(self) -> bool:
        pass

    @abstractmethod
    def set_loss_funcion(self, loss_function):
        pass
