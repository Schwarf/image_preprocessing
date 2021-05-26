from typing import Optional, Tuple

import numpy
import PIL
from contracts import contract
from data_access.files.interfaces.i_image_loader import IImageLoader
from image_factories.interfaces.i_image_from_pillow_image import IImageFromPillowImage
from image_factories.interfaces.i_pillow_resize_image import IPillowImageResize
from image_representation.implementations.image_data import ImageData
from image_representation.implementations.image_data_builder import ImageDataBuilder
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_image_data_builder import IImageDataBuilder
from pure_interface import adapt_args


class ResnetImageFromPillowImage(IImageFromPillowImage, IPillowImageResize, object):
    def __init__(self) -> None:
        self._image_builder: IImageDataBuilder = ImageDataBuilder()
        self._image_loader: Optional[IImageLoader] = None
        self._file = None
        self._image: Optional[IImageData] = None
        self._resnet_shape = (224, 224)

    @adapt_args(loader=IImageLoader)
    def set_image_loader(self, loader: IImageLoader) -> None:
        if loader is None:
            raise ValueError("ImageLoader in PillowImageFactory is 'None'.")
        self._image_loader = loader

    def _build_image(self):
        self._image_builder.set_number_of_rows(self._file.height)
        self._image_builder.set_number_of_columns(self._file.width)
        self._image_builder.set_number_of_channels(self._file.layers)
        self._image_builder.set_matrix(numpy.asarray(self._file))
        self._image_builder.set_bit_depth(self._file.bits)
        self._image_builder.set_color_mode(self._file.mode)
        self._image = ImageData(self._image_builder)

    def resize(self, new_shape: Tuple[int, int], image: PIL.Image) -> PIL.Image:
        return self._file.resize(new_shape)

    @contract(returns=IImageData)
    def next_image_from_file(self, path_to_file: str):
        self._image_loader.open(path_to_file)
        self._file = self._image_loader.get_data()
        self._file = self.resize(self._resnet_shape, self._file)
        self._build_image()
        return self._image
