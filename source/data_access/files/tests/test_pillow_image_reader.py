import mock
import PIL.Image
import pytest
from data_access.files.implementations.pillow_image_loader import PillowImageLoader


@pytest.fixture()
def full_path(tmp_path):
    path = tmp_path / "tests.jpg"
    return path


@pytest.fixture()
def invalid_full_path(tmp_path):
    path = tmp_path / "test2.jpg"
    return path


@pytest.fixture(autouse=True)
def create_tmp_file(full_path):
    file = PIL.Image.new("RGB", (1, 1))
    file.save(full_path, "PNG")
    return True


class TestPillowImageReader:
    @mock.patch.object(PIL.Image, "open")
    def test_open(self, mock, full_path, create_tmp_file):
        loader = PillowImageLoader()
        mock.assert_not_called()
        loader.open(full_path)
        mock.assert_called_once()

    def test_open_raises_with_invalid_path(self, invalid_full_path):
        loader = PillowImageLoader()
        with pytest.raises(ValueError, match="The path .*"):
            loader.open(invalid_full_path)

    @mock.patch.object(PillowImageLoader, "get_data")
    def test_read_is_called(self, mock, full_path, create_tmp_file):
        loader = PillowImageLoader()
        mock.assert_not_called()
        loader.get_data()
        mock.assert_called_once()

    @mock.patch.object(PIL.Image.Image, "close")
    def test_close_is_called(self, mock, full_path, create_tmp_file):
        loader = PillowImageLoader()
        loader.open(full_path)
        mock.assert_not_called()
        loader.close()
        mock.assert_called_once()
