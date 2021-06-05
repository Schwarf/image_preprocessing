from typing import Any

from data_access.files.interfaces.i_file_reader import IFileReader


class TensorflowRecordReader(IFileReader, object):
    def get_data(self) -> Any:
        pass

    def open(self, path_to_file) -> None:
        pass

    def close(self) -> None:
        pass
