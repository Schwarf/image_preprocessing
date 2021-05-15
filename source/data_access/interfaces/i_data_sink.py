from abc import ABC, abstractmethod
from typing import Any


class IDataSink(ABC):
    @abstractmethod
    def write(self, data: Any) -> None:
        pass
