from labels.interfaces.i_scalar_label_feature import IScalarLabelFeature


class MaxPersonCount5Label(IScalarLabelFeature, object):
    NAME = "max_person_count_5_label"

    def __init__(self, number_of_persons):
        if number_of_persons < 0:
            raise ValueError(f"Invalid number of persons. Value is {number_of_persons}.")
        if number_of_persons > 5:
            number_of_persons = 5
        self._number_of_persons = number_of_persons

    @property
    def value(self):
        return self._number_of_persons

    @property
    def name(self):
        return self.NAME
