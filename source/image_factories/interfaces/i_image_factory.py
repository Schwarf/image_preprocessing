from typing import Any

from contracts import contract
from image_representation.interfaces.i_image_data import IImageData
from pure_contracts import ContractInterface
from pure_interface import abstractmethod


class IImageFactory(ContractInterface):
    @abstractmethod
    @contract(returns=IImageData)
    def next_image(self):
        pass

    @abstractmethod
    def set_image_source(self, source: Any):
        pass
