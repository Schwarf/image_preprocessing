import json

import pytest
from data_access.files.implementations.json_file_reader import JSONFileReader


@pytest.fixture()
def full_path(tmp_path):
    full_path = tmp_path / "test.json"
    return full_path


@pytest.fixture()
def temporary_json_file(full_path):
    file = open(full_path, "w")
    data = {"json": "test file"}
    json.dump(data, file)
    file.close()
    return data


@pytest.fixture()
def temporary_text_file(full_path):
    file = open(full_path, "w")
    file.write("Hallo")
    file.close()
    return file


class TestJSONFileReader:
    def test_open_file_does_not_exist(self, full_path):
        json_reader = JSONFileReader()
        with pytest.raises(ValueError, match="The path .*"):
            json_reader.open(full_path)

    @pytest.mark.usefixtures("temporary_json_file")
    def test_open_with_file(self, full_path):
        json_reader = JSONFileReader()
        # Does not throw
        json_reader.open(full_path)

    @pytest.mark.usefixtures("temporary_text_file")
    def test_read_non_json_file(self, full_path):
        json_reader = JSONFileReader()
        json_reader.open(full_path)
        with pytest.raises(ValueError, match="The file is not a JSON file. .*"):
            json_reader.get_data()

    def test_read_json_file(self, full_path, temporary_json_file):
        json_reader = JSONFileReader()
        data_to_be = temporary_json_file
        json_reader.open(full_path)
        data = json_reader.get_data()
        assert data == data_to_be

    def test_close_file(self, full_path, temporary_json_file):
        json_reader = JSONFileReader()
        json_reader.open(full_path)
        json_reader.close()
        assert json_reader._file.closed is True
