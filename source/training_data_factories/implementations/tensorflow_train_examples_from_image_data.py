from typing import Any, Dict

import numpy
import tensorflow
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_labeled_image_data import ILabeledImageData
from labels.interfaces.i_scalar_label_feature import IScalarLabelFeature
from training_data_factories.interfaces.i_tensorflow_train_examples_from_image_data import (
    ITensorflowTrainExamplesFromImageData,
)


class TensorflowTrainExamplesFromImageData(ITensorflowTrainExamplesFromImageData, object):
    def __init__(self):
        self._image_data = None
        self._tf_feature_dictionary: Dict[str, tensorflow.train.Feature] = {}
        self._signed_integer_dictionary = {8: numpy.int8, 16: numpy.int16, 32: numpy.int32, 64: numpy.int64}
        self._unsigned_integer_dictionary = {8: numpy.uint8, 16: numpy.uint16, 32: numpy.uint32, 64: numpy.uint64}

    def _create_tensorflow_train_feature(self, data: Any) -> tensorflow.train.Feature:
        feature_data = data
        if not isinstance(data, list):
            feature_data = [data]
        return tensorflow.train.Feature(bytes_list=tensorflow.train.BytesList(value=feature_data))

    def _create_tensorflow_2d_unsigned_integer_feature_from_image_data(self):
        shape_descriptor = "shape"
        image_data_descriptor = "image_data"
        image_shape = (
            self._image_data.number_of_channels,
            self._image_data.number_of_rows,
            self._image_data.number_of_columns,
        )
        image_shape_feature = numpy.array(image_shape, dtype=numpy.int16).tobytes()
        image_data_type = self._unsigned_integer_dictionary[self._image_data.bit_depth]
        image_data_feature = self._image_data.matrix.astype(image_data_type).tobytes()
        self._tf_feature_dictionary[shape_descriptor] = self._create_tensorflow_train_feature(image_shape_feature)
        self._tf_feature_dictionary[image_data_descriptor] = self._create_tensorflow_train_feature(image_data_feature)
        if ILabeledImageData.provided_by(self._image_data, allow_implicit=True):
            for name, label in self._image_data.dict_of_label_features.items():
                if isinstance(label, IScalarLabelFeature):
                    self._tf_feature_dictionary[name] = self._create_tensorflow_train_feature(
                        numpy.int16(label.value).tobytes()
                    )

        self._image_data = None

    def set_image_data(self, image_data: IImageData) -> None:
        self._image_data = image_data

    def get_train_example(self) -> tensorflow.train.Example:
        if self._image_data is None:
            raise ValueError("Image data is 'None' in TensorflowTrainExamplesFromImageData.")
        self._create_tensorflow_2d_unsigned_integer_feature_from_image_data()
        train_example = tensorflow.train.Example(
            features=tensorflow.train.Features(feature=self._tf_feature_dictionary)
        )

        return train_example
