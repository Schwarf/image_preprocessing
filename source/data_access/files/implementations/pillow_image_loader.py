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
        return self._file

    def open(self) -> None:
        self._file = pil_image.open(self._full_path)

    def close(self) -> None:
        self._file.close()


full_path = "D:\\Data\\image_data\\images\\my_camera\\DCIM\\100___08\\IMG_0001.JPG"
file_reader = PillowImageLoader(full_path)
file_reader.open()
image = file_reader.read()
properties = [property for property in dir(image) if not property.startswith("_")]
print(properties)
file_reader.close()

x = 1
