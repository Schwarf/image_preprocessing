import json
import os
from typing import Any

from data_access.files.interfaces.i_file_reader import IFileReader


class JSONFileReader(IFileReader, object):
    def __init__(self):
        self._file = None

    def open(self, path_to_file) -> None:
        if not os.path.exists(path_to_file):
            raise ValueError(f"The path '{path_to_file}' provided to method 'open' does not exist!")
        self._file = open(path_to_file, "r")

    def get_data(self) -> Any:
        return json.load(self._file)

    def close(self) -> None:
        self._file.close()
