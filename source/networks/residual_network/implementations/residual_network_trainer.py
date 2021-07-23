from typing import Optional

import tensorflow
from networks.interfaces.i_hyper_parameters import IHyperParameters
from pure_interface import adapt_args
from training_process.interfaces.i_network_trainer import INetworkTrainer


class ResidualNetworkTrainer(INetworkTrainer, object):
    @adapt_args
    def __init__(self, hyper_parameters: IHyperParameters):
        self._model: Optional[tensorflow.keras.models.Model] = None
        self._training_input = None
        self._training_labels = None
        self._loss_function = None
        self._loss_weights = None
        self._optimizer = None
        self._training_metric = None
        self._validation_metric = None
        self._training_loss_metric = None
        self._validation_loss_metric = None
        self._hyper_parameters = hyper_parameters
        self._validation_labels = None
        self._validation_input = None

    def set_losses(self, losses, loss_weights=None):
        self._loss_function = losses
        if loss_weights is None:
            self._loss_weights = [1.0] * len(losses)

    def set_optimizer(self, optimizer):
        self._optimizer = optimizer

    def set_training_data(self, training_input, training_labels):
        self._training_input = training_input
        self._training_labels = training_labels

    @tensorflow.function
    def _train_step(self, images, labels):
        with tensorflow.GradientTape() as tape:
            predictions = self._model(images, training=True)
            training_loss = self._loss_function(y_true=labels, y_pred=predictions)
        gradients = tape.gradient(training_loss, self._model.trainable_variables)
        self._optimizer.apply_gradients(grads_and_vars=zip(gradients, self._model.trainable_variables))
        self._training_loss_metric(training_loss)
        self._training_metric(labels, predictions)

    @tensorflow.function
    def _validation_step(self, images, labels):
        predictions = self._model(images, training=False)
        validation_loss = self._loss_function(y_true=labels, y_pred=predictions)
        self._validation_loss_metric(validation_loss)
        self._validation_metric(labels, predictions)

    def run(self):
        pass

    def set_model(self, model: tensorflow.keras.models.Model):
        self._model = model

    def set_data(self, training_input, training_labels):
        self._training_input = training_input
        self._training_labels = training_labels

    def set_validation_metric(self, validation_metric):
        self._validation_metric = validation_metric

    def set_training_metric(self, training_metric):
        self._training_metric = training_metric

    def set_validation_loss_metric(self, validation_loss_metric):
        self._validation_loss_metric = validation_loss_metric

    def set_training_loss_metric(self, training_loss_metric):
        self._training_loss_metric = training_loss_metric

    def set_validation_data(self, validation_input, validation_labels):
        self._validation_input = validation_input
        self._validation_labels = validation_labels
