import numpy
from pure_interface import Interface, abstractmethod


class IImageData(Interface):
    @property
    @abstractmethod
    def matrix(self) -> numpy.ndarray:
        pass

    @property
    @abstractmethod
    def bit_depth(self) -> numpy.int8:
        pass

    @property
    @abstractmethod
    def number_of_rows(self) -> numpy.int32:
        pass

    @property
    @abstractmethod
    def number_of_columns(self) -> numpy.int32:
        pass

    @property
    @abstractmethod
    def number_of_channels(self) -> numpy.int8:
        pass

    @property
    @abstractmethod
    def color_mode(self) -> str:
        pass

    @property
    @abstractmethod
    def data_source_identifier(self) -> str:
        pass
