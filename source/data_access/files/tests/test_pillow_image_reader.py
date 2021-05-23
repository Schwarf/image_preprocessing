import mock
import pytest
from data_access.files.implementations.pillow_image_loader import PillowImageLoader


@pytest.fixture()
def full_path(tmp_path):
    path = tmp_path / "test.jpg"
    return path


@pytest.fixture()
def invalid_full_path(tmp_path):
    path = tmp_path / "test2.jpg"
    return path


@pytest.fixture()
def create_tmp_file(full_path):
    file = open(full_path, "w")
    file.close()
    return True


class TestPillowImageReader:
    @mock.patch.object(PillowImageLoader, "open")
    def test_open(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader()
        mock.assert_not_called()
        loader.open(full_path)
        mock.assert_called_once()

    def test_read_raises_without_open(self, invalid_full_path):
        loader = PillowImageLoader()
        with pytest.raises(ValueError, match="The path .*"):
            loader.open(invalid_full_path)

    @mock.patch.object(PillowImageLoader, "get_data")
    def test_read_is_called(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader()
        mock.assert_not_called()
        loader.get_data()
        mock.assert_called_once()

    @mock.patch.object(PillowImageLoader, "close")
    def test_close_is_called(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader()
        mock.assert_not_called()
        loader.close()
        mock.assert_called_once()
