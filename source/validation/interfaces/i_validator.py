from typing import Any

from pure_interface import Interface, abstractmethod


class IValidator(Interface):
    @abstractmethod
    def validate(self, input: Any) -> None:
        pass
