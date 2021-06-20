import tensorflow
from networks.residual_network.interfaces.i_residual_layer import IResidualLayer
from networks.residual_network.interfaces.i_residual_layer_parameters import IResidualLayerParameters
from pure_interface import adapt_args


class ResidualLayer(IResidualLayer, tensorflow.keras.layers.Layer, object):
    @adapt_args
    def __init__(self, builder: IResidualLayerParameters):
        super(ResidualLayer, self).__init__()
        self._number_of_kernels = builder.number_of_kernels
        self._stride_size = builder.stride_size
        self._kernel_size = builder.kernel_size
        self._padding = builder.padding
        self._name = builder.name
        self._minimal_kernel_size = (1, 1)
        self._minimal_stride_size = (1, 1)

        self._default_valid_padding = "valid"
        self._down_sample_model = None
        self._construct_residual_layer()

    def _construct_residual_layer(self):

        self._convolution_1 = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_kernels,
            kernel_size=self._kernel_size,
            strides=self._stride_size,
            padding=self._padding,
        )
        self._batch_normalization_1 = tensorflow.keras.layers.BatchNormalization()
        self._convolution_2 = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_kernels,
            kernel_size=self._kernel_size,
            strides=self._minimal_stride_size,
            padding=self._padding,
        )
        self._batch_normalization_2 = tensorflow.keras.layers.BatchNormalization()

        self._down_sample_convolution = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_kernels,
            kernel_size=self._minimal_kernel_size,
            strides=self._minimal_stride_size,
            padding=self._default_valid_padding,
        )

        self._down_sample_batch_normalization = tensorflow.keras.layers.BatchNormalization()

        if self._stride_size != 1:
            self._down_sample_model = tensorflow.keras.Sequential()
            self._down_sample_model.add(self._down_sample_convolution)
            self._down_sample_model.add(self._down_sample_batch_normalization)
        else:
            self._down_sample_model = lambda identity: identity

    def call(self, input_data, training=None, **kwargs):
        down_sample_model = self._down_sample_model(input_data)

        compute_convulution_1 = self._convolution_1(input_data)
        compute_batch_normalization_1 = self._batch_normalization_1(compute_convulution_1, training=training)
        compute_relu_activation = tensorflow.nn.relu(compute_batch_normalization_1)
        compute_convulution_2 = self._convolution_2(compute_relu_activation)
        compute_batch_normalization_2 = self._batch_normalization_2(compute_convulution_2, training=training)

        down_sample = tensorflow.keras.layers.add([down_sample_model, compute_batch_normalization_2])
        final_activation = tensorflow.nn.relu(down_sample)
        return final_activation

    def get_config(self):
        config = super(ResidualLayer, self).get_config()
        return config

    def name(self):
        return self._name
