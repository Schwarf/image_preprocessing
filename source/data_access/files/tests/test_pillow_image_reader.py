import mock
import pytest
from data_access.files.implementations.pillow_image_loader import PillowImageLoader


@pytest.fixture()
def full_path(tmp_path):
    path = tmp_path / "test.jpg"
    return path


@pytest.fixture()
def create_tmp_file(full_path):
    file = open(full_path, "w")
    file.close()
    return True


class TestPillowImageReader:
    def test_constructor_path_does_not_exist(self, full_path):
        with pytest.raises(OSError, match="The path provided to the constructor of PilloImageLoader does not exist!"):
            PillowImageLoader(full_path)

    def test_constructor_path_does_exist(self, full_path, create_tmp_file):
        create_tmp_file
        PillowImageLoader(full_path)

    @mock.patch.object(PillowImageLoader, "open")
    def test_open(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader(full_path)
        mock.assert_not_called()
        loader.open()
        mock.assert_called_once()

    def test_read_raises_without_open(self, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader(full_path)
        with pytest.raises(ValueError, match="File .*"):
            loader.read()

    @mock.patch.object(PillowImageLoader, "read")
    def test_read_is_called(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader(full_path)
        mock.assert_not_called()
        loader.read()
        mock.assert_called_once()

    @mock.patch.object(PillowImageLoader, "close")
    def test_close_is_called(self, mock, full_path, create_tmp_file):
        create_tmp_file
        loader = PillowImageLoader(full_path)
        mock.assert_not_called()
        loader.close()
        mock.assert_called_once()
