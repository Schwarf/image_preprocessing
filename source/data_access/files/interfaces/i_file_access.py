from pure_interface import Interface, abstractmethod


class IFileAccess(Interface):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
