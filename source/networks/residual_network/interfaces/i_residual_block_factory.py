from pure_interface import Interface, abstractmethod


class IResidualBlockFactory(Interface):
    @abstractmethod
    def build(self):
        pass

    @property
    @abstractmethod
    def number_of_residual_layers(self):
        pass
