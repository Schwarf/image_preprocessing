import os

import tensorflow
from data_access.files.interfaces.i_file_writer import IFileWriter


class TensorflowRecordWriter(IFileWriter, object):
    def __init__(self):
        self._file_handle = None

    def open(self, path_to_file) -> None:
        if not os.path.exists(os.path.dirname(path_to_file)):
            raise ValueError("The path provided to the 'open' method of TensorflowRecordWriter does not exist!")
        self._file_handle = tensorflow.io.TFRecordWriter(self._path_to_file)

    def write(self, data: tensorflow.train.Example()):
        self._file_handle.write(data.SerializeToString())

    def close(self):
        self._file_handle.flush()
        self._file_handle.close()
