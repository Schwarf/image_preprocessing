from data_access.files.interfaces.i_image_loader import IImageLoader
from pure_interface import Interface, abstractmethod


class IImageFromPillowImage(Interface):
    @abstractmethod
    def set_image_loader(self, loader: IImageLoader):
        pass

    @abstractmethod
    def next_image_from_file(self, path_to_file: str):
        pass
