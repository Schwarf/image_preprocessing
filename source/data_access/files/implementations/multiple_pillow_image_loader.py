from typing import Any, List

from data_access.files.implementations.pillow_image_loader import PillowImageLoader
from data_access.files.interfaces.i_multiple_image_loader import IMultipleImageLoader


class MultiplePillowImageLoader(IMultipleImageLoader, object):
    def __init__(self, list_of_full_paths: List[str]) -> None:
        if not isinstance(list_of_full_paths, list):
            raise TypeError(
                "The constructor parameter 'list_of_full_paths' in MultiplePilloImageLoader is not of type 'list'!"
            )

        if list_of_full_paths is []:
            raise ValueError("The 'list_of_full_paths' is empty!")

        if not isinstance(list_of_full_paths[0], str):
            raise ValueError("The elements of 'list_of_full_paths' are not of type 'str'!")

        self._paths_to_files = iter(list_of_full_paths)
        self._pillow_image_loader = None
        self._end = "\n list end"
        self._is_image_available = True

    def _load_next(self):
        path = next(self._paths_to_files, self._end)
        if path is self._end:
            self._is_image_available = False
            return None
        self._pillow_image_loader = PillowImageLoader(path)
        self._pillow_image_loader.open()
        data = self._pillow_image_loader.get_data()
        self._pillow_image_loader.close()
        return data

    @property
    def is_image_available(self) -> bool:
        return self._is_image_available

    def get_data(self) -> Any:
        return self._load_next()
