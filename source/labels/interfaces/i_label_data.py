from pure_interface import Interface, abstractmethod


class ILabelData(Interface):
    @abstractmethod
    def assign(self, label):
        pass

    @abstractmethod
    def set_data(self, data):
        pass
