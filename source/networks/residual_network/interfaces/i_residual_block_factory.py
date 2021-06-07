from pure_interface import Interface, abstractmethod


class IResidualBlockFactory(Interface):
    @abstractmethod
    def build_block(self):
        pass
