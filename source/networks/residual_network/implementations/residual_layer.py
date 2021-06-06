import tensorflow


class ResnetLayer(tensorflow.keras.layers.Layer):
    def __init__(self, number_of_filters, stride_size, kernel_size):
        super(ResnetLayer, self).__init__()
        if number_of_filters < 1:
            raise ValueError(f"Invalid number of filters: {number_of_filters}")
        if stride_size < 1:
            raise ValueError(f"Invalid stride size: {stride_size}")
        if kernel_size[0] < 1 or kernel_size[1] < 1:
            raise ValueError(f"Invalid kernel size: {kernel_size}")

        self._number_of_filters = number_of_filters
        self._stride_size = stride_size
        self._kernel_size = kernel_size
        self._minimal_kernel_size = (1, 1)
        self._minimal_stride_size = (1, 1)
        self._same_padding = "same"
        self._valid_padding = "valid"
        self._down_sample_model = None
        self._construct()

    def _construct(self):

        self._convolution_1 = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_filters,
            kernel_size=self._kernel_size,
            strides=self._stride_size,
            padding=self._same_padding,
        )
        self._batch_normalization_1 = tensorflow.keras.layers.BatchNormalization()
        self._convolution_2 = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_filters,
            kernel_size=self._kernel_size,
            strides=self._minimal_stride_size,
            padding=self._same_padding,
        )
        self._batch_normalization_2 = tensorflow.keras.layers.BatchNormalization()

        self._down_sample_convolution = tensorflow.keras.layers.Conv2D(
            filters=self._number_of_filters,
            kernel_size=self._minimal_kernel_size,
            strides=self._minimal_stride_size,
            padding=self._valid_padding,
        )

        self._down_sample_batch_normalization = tensorflow.keras.layers.BatchNormalization()

        if self._stride_size == 1:
            self._down_sample_model = tensorflow.keras.Sequential()
            self._down_sample_model.add(self._down_sample_convolution)
            self._down_sample_model.add(self._down_sample_batch_normalization)
        else:
            self._down_sample_model = lambda identity: identity

    def call(self, input, training=None, **kwargs):
        down_sample_model = self._down_sample_model(input)

        compute_convulution_1 = self._convolution_1(input)
        compute_batch_normalization_1 = self._batch_normalization_1(compute_convulution_1, training=training)
        compute_relu_activation = tensorflow.nn.relu(compute_batch_normalization_1)
        compute_convulution_2 = self._convolution_2(compute_relu_activation)
        compute_batch_normalization_2 = self._batch_normalization_2(compute_convulution_2, training=training)

        down_sample = tensorflow.keras.layers.add([down_sample_model, compute_batch_normalization_2])
        final_activation = tensorflow.nn.relu(down_sample)
        return final_activation
