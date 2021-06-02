from image_representation.interfaces.i_image_data import IImageData
from pure_interface import Interface, abstractmethod


class ILabeledImageData(IImageData, Interface):
    @abstractmethod
    def add_label_feature(self, label_feature):
        pass

    @property
    @abstractmethod
    def dict_of_label_features(self):
        pass
