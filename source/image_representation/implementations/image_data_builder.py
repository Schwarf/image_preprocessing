import numpy
from image_representation.interfaces.i_image_data_builder import IImageDataBuilder


class ImageDataBuilder(IImageDataBuilder, object):
    def __init(self):
        self._matrix = None
        self._bit_depth = None
        self._color_mode = None
        self._number_of_channels = None
        self._number_of_rows = None
        self._number_of_columns = None

    def set_matrix(self, matrix: numpy.ndarray) -> None:
        if matrix is None:
            raise ValueError("Matrix is 'None' in ImageBuilder!")
        self._matrix = matrix

    def set_bit_depth(self, bit_depth: numpy.int8) -> None:
        if bit_depth is None:
            raise ValueError("Bit depth is 'None' in ImageBuilder!")
        self._bit_depth = bit_depth

    def set_number_of_rows(self, number_of_rows: numpy.int32) -> None:
        if number_of_rows is None:
            raise ValueError("Number of rows is 'None' in ImageBuilder!")
        self._number_of_rows = number_of_rows

    def set_number_of_columns(self, number_of_columns: numpy.int32) -> None:
        if number_of_columns is None:
            raise ValueError("Number of columns is 'None' in ImageBuilder!")
        self._number_of_columns = number_of_columns

    def set_number_of_channels(self, number_of_channels: numpy.int8) -> None:
        if number_of_channels is None:
            raise ValueError("Number of channels is 'None' in ImageBuilder!")
        self._number_of_channels = number_of_channels

    def set_color_mode(self, color_mode: str) -> None:
        if color_mode is None:
            raise ValueError("Color mode is 'None' in ImageBuilder!")
        self._color_mode = color_mode

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
