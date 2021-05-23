from pure_interface import Interface, abstractmethod


class IFileAccess(Interface):
    @abstractmethod
    def open(self, path_to_file) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
