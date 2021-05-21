from typing import Any

from pure_interface import Interface, abstractmethod


class IImage(Interface):
    @property
    @abstractmethod
    def matrix(self) -> Any:
        pass

    @property
    @abstractmethod
    def bit_depth(self) -> Any:
        pass

    @property
    @abstractmethod
    def number_of_rows(self) -> Any:
        pass

    @property
    @abstractmethod
    def number_of_columns(self) -> Any:
        pass

    @property
    @abstractmethod
    def number_of_channels(self) -> Any:
        pass

    @property
    @abstractmethod
    def color_mode(self) -> Any:
        pass
