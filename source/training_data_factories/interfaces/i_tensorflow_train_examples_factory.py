import tensorflow
from pure_interface import Interface, abstractmethod


class ITensorflowTrainExampleFactory(Interface):
    @abstractmethod
    def get_train_example(self) -> tensorflow.train.Example:
        pass
