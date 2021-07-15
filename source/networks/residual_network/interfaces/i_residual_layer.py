from pure_interface import Interface, abstractmethod


class IResidualLayer(Interface):
    @abstractmethod
    def call(self, input_data, training=None, **kwargs):
        pass

    @abstractmethod
    def get_config(self):
        pass
