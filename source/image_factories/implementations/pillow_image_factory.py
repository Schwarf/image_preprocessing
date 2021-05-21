from typing import Optional

from contracts import contract
from data_access.files.interfaces.i_image_loader import IImageLoader
from image_factories.interfaces.i_pillow_image_factory import IPillowImageFactory
from image_representation.implementations.image_data import ImageData
from image_representation.implementations.image_data_builder import ImageDataBuilder
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_image_data_builder import IImageDataBuilder
from pure_interface import adapt_args


class PillowImageFactory(IPillowImageFactory):
    def __init__(self) -> None:
        self._image_builder: IImageDataBuilder = ImageDataBuilder()
        self._image_loader: Optional[IImageLoader] = None

    @contract(returns=IImageData)
    def next_image(self) -> IImageData:
        pass

    @adapt_args(loader=IImageLoader)
    def set_image_loader(self, loader: IImageLoader) -> None:
        if loader is None:
            raise ValueError("ImageLoader in PillowImageFactory is 'None'.")
        self._image_loader = loader
        self._image_loader.open()
