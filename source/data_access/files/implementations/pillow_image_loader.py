import os
from typing import Any

import PIL.Image as pil_image
from data_access.files.interfaces.i_image_loader import IImageLoader


class PillowImageLoader(IImageLoader, object):
    def __init__(self) -> None:
        self._file: Any = None

    def get_data(self) -> Any:
        return self._file

    def open(self, path_to_file) -> None:
        if not os.path.exists(path_to_file):
            raise ValueError(f"The path '{path_to_file}' provided to method 'open' does not exist!")
        self._file = pil_image.open(path_to_file)

    def close(self) -> None:
        self._file.close()
        self._file = None
