import pytest
from labels.implementations.max_person_count_5_label import MaxPersonCount5Label


class TestMaxPersonCount5Label:
    def test_valid_person_count_below5(self):
        number_of_persons = 5
        label = MaxPersonCount5Label(number_of_persons)
        assert label.value == number_of_persons

    def test_valid_person_count_above5(self):
        number_of_persons = 8
        label = MaxPersonCount5Label(number_of_persons)
        max_number_of_persons = 5
        assert label.value == max_number_of_persons

    def test_invalid_person_count(self):
        number_of_persons = -1
        with pytest.raises(ValueError, match="Invalid number of persons. .*"):
            MaxPersonCount5Label(number_of_persons)

    def test_name(self):
        name = "max_person_count_5_label"
        label = MaxPersonCount5Label(number_of_persons=0)
        assert label.name is name
