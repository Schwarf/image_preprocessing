from labels.interfaces.i_person_count_label import IPersonCountLabel


class PersonCountLabel(IPersonCountLabel, object):
    NAME = "person_count_label"

    def __init__(self, number_of_persons):
        if number_of_persons < 0:
            raise ValueError(f"Invalid number of persons. Value is {number_of_persons}.")
        self._number_of_persons = number_of_persons

    @property
    def number_of_persons(self):
        return self._number_of_persons

    @property
    def name(self):
        return self.NAME
