import tensorflow
from networks.residual_network.implementations.residual_block_factory import ResidualBlockFactory
from networks.residual_network.interfaces.i_residual_model import IResidualModel


class ResidualModel(IResidualModel, tensorflow.keras.Model, object):
    def __init__(
        self,
        number_of_residual_layers_1,
        number_of_residual_layers_2,
        number_of_residual_layers_3,
        number_of_residual_layers_4,
        number_of_classes,
    ):
        super(ResidualModel, self).__init__()

        self._convolution = tensorflow.keras.layers.Conv2D(
            filters=64, kernel_size=(7, 7), strides=2, padding="same", use_bias=False
        )
        self._batch_normalization = tensorflow.keras.layers.BatchNormalization()
        self._max_pooling = tensorflow.keras.layers.MaxPool2D(pool_size=(3, 3), strides=2, padding="same")

        block_factory_1 = ResidualBlockFactory(
            number_of_residual_layers=number_of_residual_layers_1, number_of_kernels=64, stride_size=1
        )

        block_factory_2 = ResidualBlockFactory(
            number_of_residual_layers=number_of_residual_layers_2, number_of_kernels=128, stride_size=2
        )

        block_factory_3 = ResidualBlockFactory(
            number_of_residual_layers=number_of_residual_layers_3, number_of_kernels=256, stride_size=2
        )

        block_factory_4 = ResidualBlockFactory(
            number_of_residual_layers=number_of_residual_layers_4, number_of_kernels=512, stride_size=2
        )

        self._residual_block_1 = block_factory_1.build_block()
        self._residual_block_2 = block_factory_2.build_block()
        self._residual_block_3 = block_factory_3.build_block()
        self._residual_block_4 = block_factory_4.build_block()

        self._average_pooling = tensorflow.keras.layers.GlobalAveragePooling2D()
        self._fully_connected = tensorflow.keras.layers.Dense(
            units=number_of_classes, activation=tensorflow.keras.activations.softmax, use_bias=False
        )

    def call(self, input_data, training):
        convolution = self._convolution(input_data)
        batch_normalization = self._batch_normalization(convolution, training=training)
        relu_activation = tensorflow.nn.relu(batch_normalization)
        max_pooling = self._max_pooling(relu_activation)
        residual_block_1 = self._residual_block_1(max_pooling, training=training)
        residual_block_2 = self._residual_block_2(residual_block_1, training=training)
        residual_block_3 = self._residual_block_3(residual_block_2, training=training)
        residual_block_4 = self._residual_block_4(residual_block_3, training=training)
        average_pooling = self._average_pooling(residual_block_4)
        output = self._fully_connected(average_pooling)
        return output

    def get_config(self):
        super().get_config()
