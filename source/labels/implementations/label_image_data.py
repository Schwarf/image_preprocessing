from typing import Optional

from contracts import contract
from image_representation.implementations.labeled_image_data import LabeledImageData
from image_representation.interfaces.i_image_data import IImageData
from image_representation.interfaces.i_labeled_image_data import ILabeledImageData
from labels.interfaces.i_label_data import ILabelData
from labels.interfaces.i_scalar_label_feature import IScalarLabelFeature
from pure_interface import Interface, abstractmethod, adapt_args


class LabelImageData(ILabelData, object):
    def __init__(self):
        self._labeled_image_data: Optional[ILabeledImageData] = None

    @contract(returns=ILabeledImageData)
    @adapt_args(label=IScalarLabelFeature)
    def assign(self, label):
        if self._labeled_image_data is None:
            raise ValueError("Can not assign label, because labeled image data is 'None'!")
        if label is None:
            raise ValueError("Label is 'None'!")
        self._labeled_image_data.add_label_feature(label)
        return self._labeled_image_data

    @adapt_args(data=IImageData)
    def set_data(self, data):
        if data is None:
            raise ValueError("Image data is 'None'!")
        self._labeled_image_data = LabeledImageData(data)
