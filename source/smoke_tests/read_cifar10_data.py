import numpy
from data_access.files.implementations.pickle_file_reader import PickleFileReader
from PIL import Image

encoding = "bytes"

reader = PickleFileReader(encoding=encoding)
file_path = "/media/linux_data/data/cifar10/cifar-10-batches-py/data_batch_1"
reader.open(file_path)

data = reader.get_data()
image = data[b"data"][2]
image = numpy.swapaxes(numpy.swapaxes(image.reshape((3, 32, 32)), 0, 2), 0, 1)
img = Image.fromarray(image, "RGB")
img.show()
# x = 1
