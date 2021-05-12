from abc import ABC, abstractmethod
from typing import Any


class IImage(ABC):
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
