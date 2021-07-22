import pickle
import os
from typing import Any

from data_access.files.interfaces.i_file_reader import IFileReader


class PickleFileReader(IFileReader, object):
    possible_encodings = ['ASCII', 'bytes', 'latin1']

    def __init__(self, encoding):
        if encoding not in self.possible_encodings:
            raise ValueError(f"The encoding '{encoding}' is not a valid pickle-encoding!")
        self._encoding = encoding
        self._file = None

    def open(self, path_to_file) -> None:
        if not os.path.exists(path_to_file):
            raise ValueError(f"The path '{path_to_file}' provided to method 'open' does not exist!")
        self._file = open(path_to_file, "rb")

    def get_data(self) -> Any:
        try:
            data = pickle.load(self._file, encoding=self._encoding)
        except ValueError as error:
            raise ValueError("The file is not a python-pickle file. The original error message is: .") from error
        return data

    def close(self) -> None:
        self._file.close()
