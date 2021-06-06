from pure_interface import Interface, abstractmethod


class IHyperParameters(Interface):
    @property
    @abstractmethod
    def number_of_epochs(self):
        pass

    @property
    @abstractmethod
    def initial_learning_rate(self):
        pass

    @property
    @abstractmethod
    def batch_size(self):
        pass
