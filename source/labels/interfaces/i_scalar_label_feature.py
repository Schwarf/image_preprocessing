from pure_interface import Interface, abstractmethod


class IScalarLabelFeature(Interface):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def value(self):
        pass
