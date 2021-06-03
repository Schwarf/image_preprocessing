import argparse

from data_access.files.implementations.json_file_reader import JSONFileReader
from data_access.files.implementations.pillow_image_loader import PillowImageLoader
from data_access.files.implementations.tensorflow_record_writer import TensorflowRecordWriter
from image_factories.implementations.resnet_image_from_pillow_image import ResnetImageFromPillowImage
from image_representation.interfaces.i_labeled_image_data import ILabeledImageData
from labels.implementations.label_image_data import LabelImageData
from labels.implementations.max_person_count_5_label import MaxPersonCount5Label
from training_data_factories.implementations.tensorflow_train_examples_from_image_data import (
    TensorflowTrainExamplesFromImageData,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate RESNET training data")
    parser.add_argument("--labeled_data_file", default=None, type=str)
    parser.add_argument("--tf_record_destination", default=None, type=str)

    cl_args = parser.parse_args()
    json_file_reader = JSONFileReader()
    json_file_reader.open(cl_args.labeled_data_file)
    file_path_to_label_mapping = json_file_reader.get_data()
    json_file_reader.close()

    invalid_label = -1
    image_factory = ResnetImageFromPillowImage()
    image_loader = PillowImageLoader()
    image_factory.set_image_loader(image_loader)
    training_data_factory = TensorflowTrainExamplesFromImageData()
    tensorflow_record_writer = TensorflowRecordWriter()
    record_name = "image_data_record"
    record_suffix = ".tf_record"
    for index, (file_path, label) in enumerate(file_path_to_label_mapping.items()):
        if label == invalid_label:
            continue
        image_data = image_factory.next_image_from_file(file_path)
        label_image_data = LabelImageData()
        label_image_data.set_data(image_data)
        max_person_5_label = MaxPersonCount5Label(label)
        labeled_image_data = label_image_data.assign(max_person_5_label)

        training_data_factory.set_image_data(labeled_image_data)

        full_record_path = cl_args.tf_record_destination + record_name + str(index) + record_suffix
        tensorflow_record_writer.open(full_record_path)
        tensorflow_record_writer.write(training_data_factory.get_train_example())
        tensorflow_record_writer.close()
