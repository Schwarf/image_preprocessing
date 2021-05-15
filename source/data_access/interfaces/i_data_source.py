from abc import ABC, abstractmethod
from typing import Any


class IDataSource(ABC):
    @abstractmethod
    def read(self) -> Any:
        pass
