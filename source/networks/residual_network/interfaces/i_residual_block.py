from pure_interface import Interface, abstractmethod


class IResidualLayer(Interface):
    @abstractmethod
    def call(self, inputs, training):
        pass

    @property
    @abstractmethod
    def number_of_strides(self):
        pass

    @property
    @abstractmethod
    def number_of_kernels(self):
        pass
