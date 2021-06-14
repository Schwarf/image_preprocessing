from pure_interface import Interface, abstractmethod


class IResidualModel(Interface):
    @abstractmethod
    def call(self, input_data, training):
        pass

    @abstractmethod
    def get_config(self):
        pass
