from typing import Any

from pure_interface import Interface, abstractmethod


class IDataSink(Interface):
    @abstractmethod
    def write(self, data: Any) -> None:
        pass
