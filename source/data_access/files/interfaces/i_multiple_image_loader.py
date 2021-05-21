from data_access.interfaces.i_data_source import IDataSource
from pure_interface import Interface, abstractmethod


class IMultipleImageLoader(IDataSource, Interface):
    @property
    @abstractmethod
    def is_image_available(self) -> bool:
        pass
