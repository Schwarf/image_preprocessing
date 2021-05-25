import mock
import numpy
import pytest
from image_representation.implementations.image_data_builder import ImageDataBuilder


class TestImageDataBuilder:
    @pytest.mark.parametrize(
        "scalar_property, property_value, exception_text",
        [
            ["bit_depth", 8, "Bit depth .*"],
            ["number_of_rows", 256, "Number of rows .*"],
            ["number_of_columns", 12, "Number of columns .*"],
            ["number_of_channels", 3, "Number of channels .*"],
            ["color_mode", "RGB", "Color mode .*"],
            ["data_source_identifier", "D:\\some\\file", "Data source identifier .*"],
        ],
    )
    def test_scalar_properties_and_set_methods(self, scalar_property, property_value, exception_text):
        builder = ImageDataBuilder()
        with pytest.raises(ValueError, match=exception_text):
            getattr(builder, scalar_property)
        set_method = "set_" + scalar_property
        getattr(builder, set_method)(property_value)
        assert getattr(builder, scalar_property) is not None
        assert getattr(builder, scalar_property) is property_value

    @pytest.mark.parametrize(
        "array_property, property_value, exception_text",
        [
            ["matrix", numpy.ones((20, 20)), "Matrix .*"],
        ],
    )
    def test_array_like_properties_and_set_methods(self, array_property, property_value, exception_text):
        builder = ImageDataBuilder()
        with pytest.raises(ValueError, match=exception_text):
            getattr(builder, array_property)
        set_method = "set_" + array_property
        getattr(builder, set_method)(property_value)
        assert getattr(builder, array_property) is not None
        numpy.testing.assert_array_equal(getattr(builder, array_property), property_value)
