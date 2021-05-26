from abc import ABC, abstractmethod
from typing import Tuple

import PIL


class IPillowImageResize(ABC):
    @abstractmethod
    def resize(self, new_shape: Tuple[int, int], image: PIL.Image) -> PIL.Image:
        pass
