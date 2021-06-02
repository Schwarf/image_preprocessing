from typing import Dict

import numpy
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_labeled_image_data import ILabeledImageData
from labels.interfaces.i_label_feature import ILabelFeature
from pure_interface import adapt_args


class LabeledImageData(ILabeledImageData, object):
    @adapt_args(image_data=IImageData)
    def __init__(self, image_data: IImageData):
        self._image_data = image_data
        self._dict_of_label_features: Dict[str, ILabelFeature] = {}

    @property
    def matrix(self) -> numpy.ndarray:
        return self._image_data.matrix

    @property
    def bit_depth(self) -> numpy.int8:
        return self._image_data.bit_depth

    @property
    def number_of_rows(self) -> numpy.int32:
        return self._image_data.number_of_rows

    @property
    def number_of_columns(self) -> numpy.int32:
        return self._image_data.number_of_columns

    @property
    def number_of_channels(self) -> numpy.int8:
        return self._image_data.number_of_channels

    @property
    def color_mode(self) -> str:
        return self._image_data.color_mode

    @property
    def data_source_identifier(self) -> str:
        return self._image_data.data_source_identifier

    @adapt_args(label_feature=ILabelFeature)
    def add_label_feature(self, label_feature):
        if label_feature.name in self._dict_of_label_features.keys():
            raise KeyError(f"The name of the label '{label_feature.name}' already exists in dictionary!")
        self._dict_of_label_features[label_feature.name] = label_feature

    @property
    def dict_of_label_features(self):
        return self._dict_of_label_features
