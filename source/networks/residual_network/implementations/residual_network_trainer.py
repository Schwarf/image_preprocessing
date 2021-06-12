from typing import Optional

import tensorflow
from networks.interfaces.i_hyper_parameters import IHyperParameters
from networks.interfaces.i_network_trainer import INetworkTrainer
from pure_interface import adapt_args


class ResidualNetworkTrainer(INetworkTrainer, object):
    @adapt_args
    def __init__(self, hyper_parameters: IHyperParameters):
        self._model: Optional[tensorflow.keras.models.Model] = None
        self._training_input = None
        self._training_labels = None
        self._losses = None
        self._loss_weights = None
        self._optimizer = None
        self._metrics = None
        self._hyper_parameters = hyper_parameters
        self._validation_labels = None
        self._validation_input = None

    def set_losses(self, losses, loss_weights=None):
        self._losses = losses
        if loss_weights is None:
            self._loss_weights = [1.0] * len(losses)

    def set_optimizer(self, optimizer):
        self._optimizer = optimizer

    def set_training_data(self, training_input, training_labels):
        self._training_input = training_input
        self._training_labels = training_labels

    #    def _get_training_and_validation_batch(self):

    def train(self):
        self._model.compile(optimizer=self._optimizer, loss=self._losses, loss_weights=self._loss_weights)

    def set_model(self, model: tensorflow.keras.models.Model):
        self._model = model

    def set_data(self, training_input, training_labels):
        self._training_input = training_input
        self._training_labels = training_labels

    def set_metrics(self, metrics):
        self._metrics = metrics

    def set_validation_data(self, validation_input, validation_labels):
        self._validation_input = validation_input
        self._validation_labels = validation_labels
