from abc import ABC, abstractmethod
from typing import Any, Tuple


class IPillowImageResize(ABC):
    @abstractmethod
    def resize(self, new_shape: Tuple[int, int], image: Any) -> Any:
        pass
