import tensorflow
from networks.residual_network.implementations.residual_model import ResidualModel

tensorflow.keras.backend.set_image_data_format("channels_last")

resnet_model18 = ResidualModel(2, 2, 2, 2, 1000)
resnet_model18.build(input_shape=(None, 224, 224, 3))
resnet_model18.summary()
# resnet_model34 = ResidualModel(3, 4, 6, 3, 1000)
# resnet_model34.build(input_shape=(None, 224, 224, 3))
# resnet_model34.summary()

loss_function = tensorflow.keras.losses.SparseCategoricalCrossentropy()
optimizer = tensorflow.keras.optimizers.Adadelta()

training_loss = tensorflow.keras.metrics.Mean(name="training_loss")
training_accuracy = tensorflow.keras.metrics.SparseCategoricalCrossentropy(name="training_accuracy")

validation_loss = tensorflow.keras.metrics.Mean(name="validation_loss")
validation_accuracy = tensorflow.keras.metrics.SparseCategoricalCrossentropy(name="validation_accuracy")
