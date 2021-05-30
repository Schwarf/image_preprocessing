import mock
import numpy
import pytest
import tensorflow
from training_data_factories.implementations.tensorflow_train_examples_from_image_data import (
    TensorflowTrainExamplesFromImageData,
)


class TestTensorflowTrainExamplesFromImageData:
    @mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
    def test_set_image_data(self, mock_image_data):
        factory = TensorflowTrainExamplesFromImageData()
        assert factory._image_data is None
        factory.set_image_data(mock_image_data)
        assert factory._image_data is not None

    def test_get_train_example_raises(self):
        factory = TensorflowTrainExamplesFromImageData()
        with pytest.raises(ValueError, match="Image data is 'None'.*"):
            factory.get_train_example()

    @mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
    @mock.patch.object(tensorflow.train, "Example")
    def test_get_train_example(self, mock, mock_image_data):
        mock_image_data.bit_depth = 8
        mock_image_data.matrix = numpy.array([1, 2, 3])
        factory = TensorflowTrainExamplesFromImageData()
        factory.set_image_data(mock_image_data)
        mock.assert_not_called()
        factory.get_train_example()
        mock.assert_called_once()
