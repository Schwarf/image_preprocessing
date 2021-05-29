from data_access.files.implementations.pillow_image_loader import PillowImageLoader
from data_access.files.implementations.tensorflow_record_writer import TensorflowRecordWriter
from image_factories.implementations.resnet_image_from_pillow_image import ResnetImageFromPillowImage
from training_data_factories.implementations.tensorflow_train_examples_from_image_data import (
    TensorflowTrainExamplesFromImageData,
)

image_factory = ResnetImageFromPillowImage()
path = None
output_path = None
image_loader = PillowImageLoader()

image_factory.set_image_loader(image_loader)

image = image_factory.next_image_from_file(path)
training_data_factory = TensorflowTrainExamplesFromImageData()
training_data_factory.set_image_data(image)
tensorflow_example = training_data_factory.get_train_example()
tensorflow_record_writer = TensorflowRecordWriter()
tensorflow_record_writer.open(output_path)
tensorflow_record_writer.write(tensorflow_example)
tensorflow_record_writer.close()
