import numpy
from pure_interface import Interface, abstractmethod


class ILabelFeature(Interface):
    @property
    @abstractmethod
    def name(self):
        pass
