import mock
import numpy
import pytest
from image_representation.implementations.image_data import ImageData


class TestImageData:
    @mock.patch("image_representation.interfaces.i_image_data_builder.IImageDataBuilder", autospec=True)
    @pytest.mark.parametrize(
        "scalar_property, property_value",
        [
            ["bit_depth", 8],
            ["number_of_rows", 256],
            ["number_of_columns", 12],
            ["number_of_channels", 3],
            ["color_mode", "RGB"],
        ],
    )
    def test_scalar_properties(self, mock_image_builder, scalar_property, property_value):
        setattr(mock_image_builder, scalar_property, property_value)
        image = ImageData(mock_image_builder)
        assert getattr(image, scalar_property) is not None
        assert getattr(image, scalar_property) is property_value

    @mock.patch("image_representation.interfaces.i_image_data_builder.IImageDataBuilder", autospec=True)
    @pytest.mark.parametrize(
        "array_property, property_value",
        [
            ["matrix", numpy.ones((20, 20, 4)) + 2.0],
        ],
    )
    def test_array_like_properties(self, mock_image_builder, array_property, property_value):
        setattr(mock_image_builder, array_property, property_value)
        image = ImageData(mock_image_builder)
        assert getattr(image, array_property) is not None
        numpy.testing.assert_array_equal(getattr(image, array_property), property_value)
