from pure_interface import Interface, abstractmethod


class ITensorflowOptimizer(Interface):
    @abstractmethod
    def get_config(self):
        pass
