import numpy
from data_access.files.implementations.pickle_file_reader import PickleFileReader
from PIL import Image

encoding = "bytes"

reader = PickleFileReader(encoding=encoding)
image_batch_list = []
label_batch_list = []

for i in range(1, 6):
    file_path = "/media/linux_data/data/cifar10/cifar-10-batches-py/data_batch_" + str(i)
    reader.open(file_path)
    data = reader.get_data()
    images = data[b"data"]
    labels = data[b"labels"]
    images = images.reshape(10000, 3072)
    labels = numpy.array(labels)
    reader.close()
    image_batch_list.append(images)
    label_batch_list.append(labels)
training_images = numpy.concatenate(image_batch_list)
training_labels = numpy.concatenate(label_batch_list)
training_images = numpy.swapaxes(numpy.swapaxes(training_images.reshape((50000, 3, 32, 32)), 1, 3), 1, 2)

file_path = "/media/linux_data/data/cifar10/cifar-10-batches-py/test_batch"
reader.open(file_path)
data = reader.get_data()
validation_images = data[b"data"]
validation_labels = data[b"labels"]
reader.close()
validation_images = validation_images.reshape(10000, 3072)
validation_labels = numpy.array(validation_labels)


image = training_images[89]
img = Image.fromarray(image, "RGB")
img.show()
