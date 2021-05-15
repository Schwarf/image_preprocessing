from abc import ABC, abstractmethod
from typing import Any


class IValidator(ABC):
    def validate(self, input: Any) -> None:
        pass
