import mock
import pytest
from image_factories.implementations.resnet_image_from_pillow_image import PillowImageFactory
from pure_interface import AdaptionError


class TestPillowImageFactory:
    @mock.patch("data_access.files.interfaces.i_image_loader.IImageLoader", autospec=True)
    def test_set_valid_image_loader(self, mock_loader):
        factory = PillowImageFactory()
        factory.set_image_loader(mock_loader)

    @mock.patch("data_access.files.interfaces.i_file_reader.IFileReader", autospec=True)
    def test_set_invalid_image_loader(self, invalid_mock_loader):
        factory = PillowImageFactory()
        with pytest.raises(AdaptionError, match="Cannot adapt .*"):
            factory.set_image_loader(invalid_mock_loader)

    def test_set_image_loader_to_none(self):
        factory = PillowImageFactory()
        mock_loader = None
        with pytest.raises(ValueError, match="ImageLoader in PillowImageFactory is 'None'."):
            factory.set_image_loader(mock_loader)

    @mock.patch.object(PillowImageFactory, "next_image_from_file")
    def test_next_image_from_file(self, mock):
        factory = PillowImageFactory()
        path = "point_to_somewhere"
        factory.next_image_from_file(path)
        mock.assert_called_once()
