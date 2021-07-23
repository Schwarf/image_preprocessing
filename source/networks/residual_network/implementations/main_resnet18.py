import tensorflow
from data_access.files.implementations.pickle_file_reader import PickleFileReader
from networks.implementations.hyper_parameters import HyperParameters
from networks.residual_network.implementations.residual_model import ResidualModel
from networks.residual_network.implementations.residual_network_trainer import ResidualNetworkTrainer

tensorflow.keras.backend.set_image_data_format("channels_last")
encoding = "bytes"


resnet_model18 = ResidualModel(2, 2, 2, 2, 1000)
resnet_model18.build(input_shape=(None, 224, 224, 3))
resnet_model18.summary()
# resnet_model34 = ResidualModel(3, 4, 6, 3, 1000)
# resnet_model34.build(input_shape=(None, 224, 224, 3))
# resnet_model34.summary()

hyper_parameters = HyperParameters(learning_rate=1.0e-4, batch_size=128, number_of_epochs=1000)

loss_function = tensorflow.keras.losses.SparseCategoricalCrossentropy()
optimizer = tensorflow.keras.optimizers.Adadelta()

training_loss_metric = tensorflow.keras.metrics.Mean(name="training_loss")
training_metric = tensorflow.keras.metrics.SparseCategoricalCrossentropy(name="training_accuracy")

validation_loss_metric = tensorflow.keras.metrics.Mean(name="validation_loss")
validation_metric = tensorflow.keras.metrics.SparseCategoricalCrossentropy(name="validation_accuracy")

trainer = ResidualNetworkTrainer()
trainer.set_model(resnet_model18)
trainer.set_losses(loss_function)
trainer.set_optimizer(optimizer)
trainer.set_validation_metric(validation_metric)
trainer.set_training_metric(training_metric)
trainer.set_validation_loss_metric(validation_loss_metric)
trainer.set_training_loss_metric(training_loss_metric)
