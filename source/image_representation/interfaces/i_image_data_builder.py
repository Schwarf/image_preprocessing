from typing import Any

import numpy
from image_representation.interfaces.i_image_data import IImageData
from pure_interface import Interface, abstractmethod


class IImageDataBuilder(IImageData, Interface):
    @abstractmethod
    def set_matrix(self, matrix: numpy.ndarray) -> None:
        pass

    @abstractmethod
    def set_bit_depth(self, bit_depth: numpy.int8) -> None:
        pass

    @abstractmethod
    def set_number_of_rows(self, number_of_rows: numpy.int32) -> None:
        pass

    @abstractmethod
    def set_number_of_columns(self, number_of_columns: numpy.int32) -> None:
        pass

    @abstractmethod
    def set_number_of_channels(self, number_of_channels: numpy.int8) -> None:
        pass

    @abstractmethod
    def set_color_mode(self, color_mode: str) -> None:
        pass
