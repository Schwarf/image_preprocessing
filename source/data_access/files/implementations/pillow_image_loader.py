import os
from typing import Any

import PIL.Image as pil_image
from data_access.files.interfaces.i_image_loader import IImageLoader


class PillowImageLoader(IImageLoader, object):
    def __init__(self, full_path: str) -> None:
        if not os.path.exists(full_path):
            raise OSError("The path provided to the constructor of PilloImageLoader does not exist!")
        self._full_path: str = full_path
        self._file: Any = None

    def read(self) -> Any:
        if self._file is None:
            raise ValueError(f"File {self._file} in PillowImageLoader has not been opened yet.")
        return self._file

    def open(self) -> None:
        self._file = pil_image.open(self._full_path)

    def close(self) -> None:
        self._file.close()
        self._file = None
