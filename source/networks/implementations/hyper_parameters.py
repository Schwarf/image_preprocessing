from networks.interfaces.i_hyper_parameters import IHyperParameters


class HyperParameters(IHyperParameters, object):
    def __init__(self, number_of_epochs: int, learning_rate: float, batch_size: int):
        self._learning_rate = learning_rate
        self._batch_size = batch_size
        self._number_of_epochs = number_of_epochs

    @property
    def number_of_epochs(self):
        return self._number_of_epochs

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def batch_size(self):
        return self._batch_size
