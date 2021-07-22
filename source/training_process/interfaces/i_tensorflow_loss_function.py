from pure_interface import Interface, abstractmethod


class ITensorflowLossFunction(Interface):
    @abstractmethod
    def call(self, y_true, y_pred):
        pass
