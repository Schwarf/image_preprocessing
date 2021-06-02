from labels.interfaces.i_label_feature import ILabelFeature
from pure_interface import Interface, abstractmethod


class IPersonCountLabel(ILabelFeature, Interface):
    @property
    @abstractmethod
    def number_of_persons(self):
        pass
