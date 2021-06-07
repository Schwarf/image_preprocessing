from networks.residual_network.interfaces.i_residual_layer_parameters import IResidualLayerParameters


class ResiduaLayerParameters(IResidualLayerParameters, object):
    VALID_PADDING = "valid"
    SAME_PADDING = "same"

    def __init__(self):
        self._number_of_kernels = None
        self._kernel_size = None
        self._stride_size = None
        self._padding = None

    @property
    def number_of_kernels(self):
        if self._number_of_kernels is None:
            raise ValueError("Number of kernels is None!")
        if self._number_of_kernels < 1:
            raise ValueError(f"Invalid number of kernels: {self._number_of_kernels}")
        return self._number_of_kernels

    @property
    def kernel_size(self):
        if self._kernel_size is None:
            raise ValueError("Kernel size is None!")
        if self._kernel_size[0] < 1 or self._kernel_size[1] < 1:
            raise ValueError(f"Invalid kernel size: {self._kernel_size}")
        return self._kernel_size

    @property
    def stride_size(self):
        if self._stride_size is None:
            raise ValueError("Stride size is None!")
        if self._stride_size < 1:
            raise ValueError(f"Invalid stride size: {self._stride_size}")
        return self._stride_size

    @property
    def padding(self):
        if self._padding is None:
            raise ValueError("Padding is None!")
        if self._padding is not self.VALID_PADDING and self._padding is not self.SAME_PADDING:
            raise ValueError(f"Padding is invalid: {self._padding}")
        return self._padding

    def set_number_of_kernels(self, number_of_kernels):
        self._number_of_kernels = number_of_kernels

    def set_kernel_size(self, kernel_size):
        self._kernel_size = kernel_size

    def set_stride_size(self, stride_size):
        self._stride_size = stride_size

    def set_padding(self, padding):
        self._padding = padding
