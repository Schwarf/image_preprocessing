import os

import tensorflow
from data_access.files.interfaces.i_file_writer import IFileWriter


class TensorflowRecordWriter(IFileWriter, object):
    def __init__(self, path_to_file: str):
        self._file_handle = None
        if not os.path.exists(os.path.dirname(path_to_file)):
            raise OSError("The path provided to the constructor of TensorflowRecordWriter does not exist!")
        self._path_to_file = path_to_file

    def open(self) -> None:
        self._file_handle = tensorflow.io.TFRecordWriter(self._path_to_file)

    def write(self, data: tensorflow.train.Example()):
        self._file_handle.write(data.SerializeToString())

    def close(self):
        self._file_handle.flush()
        self._file_handle.close()
