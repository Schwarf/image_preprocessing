from image_factories.interfaces.i_image_factory import IImageFactory
from image_representation.implementations.image_data import ImageData
from image_representation.implementations.image_data_builder import ImageDataBuilder


class ImageFactory(IImageFactory):
    def __init__(self):
        self._pillow_image = None
        self._image_builder = ImageDataBuilder()

    def next_image(self):
        pass
