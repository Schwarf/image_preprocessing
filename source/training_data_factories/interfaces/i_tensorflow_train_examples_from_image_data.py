from image_representation.interfaces.i_image_data import IImageData
from pure_interface import Interface, abstractmethod
from training_data_factories.interfaces.i_tensorflow_train_examples_factory import ITensorflowTrainExampleFactory


class ITensorflowTrainExamplesFromImageData(ITensorflowTrainExampleFactory, Interface):
    @abstractmethod
    def set_image_data(self, image_data: IImageData) -> None:
        pass
