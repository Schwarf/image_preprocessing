import numpy
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_image_data_builder import IImageDataBuilder


class ImageData(IImageData, object):
    def __init__(self, image_builder: IImageDataBuilder):
        self._matrix = image_builder.matrix
        self._bit_depth = image_builder.bit_depth
        self._color_mode = image_builder.color_mode
        self._number_of_columns = image_builder.number_of_columns
        self._number_of_rows = image_builder.number_of_rows
        self._number_of_channels = image_builder.number_of_channels
        self._data_source_identifier = image_builder.data_source_identifier

    @property
    def matrix(self) -> numpy.ndarray:
        return self._matrix

    @property
    def bit_depth(self) -> numpy.int8:
        return self._bit_depth

    @property
    def number_of_rows(self) -> numpy.int32:
        return self._number_of_rows

    @property
    def number_of_columns(self) -> numpy.int32:
        return self._number_of_columns

    @property
    def number_of_channels(self) -> numpy.int8:
        return self._number_of_channels

    @property
    def color_mode(self) -> str:
        return self._color_mode

    @property
    def data_source_identifier(self) -> str:
        return self._data_source_identifier
