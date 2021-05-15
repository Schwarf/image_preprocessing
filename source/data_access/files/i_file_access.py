from abc import ABC, abstractmethod


class IFileAccess(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
