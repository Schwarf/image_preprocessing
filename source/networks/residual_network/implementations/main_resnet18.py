import tensorflow
from networks.residual_network.implementations.residual_model import ResidualModel

tensorflow.keras.backend.set_image_data_format("channels_last")

model = ResidualModel(2, 2, 2, 2, 10)
model.build(input_shape=(None, 224, 224, 3))
model.summary()
