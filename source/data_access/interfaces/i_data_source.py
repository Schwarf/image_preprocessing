from typing import Any

from pure_interface import Interface, abstractmethod


class IDataSource(Interface):
    @abstractmethod
    def get_data(self) -> Any:
        pass
