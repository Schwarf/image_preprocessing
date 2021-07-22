import tensorflow
from networks.residual_network.implementations.residual_layer import ResidualLayer
from networks.residual_network.implementations.residual_layer_parameters import ResiduaLayerParameters
from networks.residual_network.interfaces.i_residual_block_factory import IResidualBlockFactory


class ResidualBlockFactory(IResidualBlockFactory, object):
    def __init__(self, number_of_residual_layers, number_of_kernels, stride_size):
        self._layer_parameters = ResiduaLayerParameters()
        kernel_size = (3, 3)
        self._layer_parameters.set_kernel_size(kernel_size=kernel_size)
        self._layer_parameters.set_padding("same")
        self._layer_parameters.set_number_of_kernels(number_of_kernels)
        self._layer_parameters.set_stride_size(stride_size)
        self._number_of_residual_layers = number_of_residual_layers

    def build_block(self):
        residual_block = tensorflow.keras.Sequential()
        first_residual_layer = ResidualLayer(self._layer_parameters)
        residual_block.add(first_residual_layer)
        self._layer_parameters.set_stride_size(1)
        for layer_index in range(1, self._number_of_residual_layers):
            layer = ResidualLayer(self._layer_parameters)
            residual_block.add(layer)
        return residual_block
