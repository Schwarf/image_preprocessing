from typing import Any

from pure_interface import Interface, abstractmethod


class IDataSource(Interface):
    @abstractmethod
    def read(self) -> Any:
        pass
