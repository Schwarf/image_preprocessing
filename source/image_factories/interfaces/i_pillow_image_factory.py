from data_access.files.interfaces.i_image_loader import IImageLoader
from image_factories.interfaces.i_image_factory import IImageFactory
from pure_interface import Interface, abstractmethod, adapt_args


class IPillowImageFactory(IImageFactory, Interface):
    @abstractmethod
    @adapt_args(source=IImageLoader)
    def set_image_loader(self, loader: IImageLoader):
        pass
