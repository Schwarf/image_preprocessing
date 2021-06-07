from pure_interface import Interface, abstractmethod


class IResidualLayerParameters(Interface):
    @property
    @abstractmethod
    def padding(self):
        pass

    @property
    @abstractmethod
    def number_of_kernels(self):
        pass

    @property
    @abstractmethod
    def kernel_size(self):
        pass

    @property
    @abstractmethod
    def stride_size(self):
        pass

    @abstractmethod
    def set_number_of_kernels(self, number_of_kernels):
        pass

    @abstractmethod
    def set_kernel_size(self, kernel_size):
        pass

    @abstractmethod
    def set_stride_size(self, stride_size):
        pass

    @abstractmethod
    def set_padding(self, padding):
        pass
