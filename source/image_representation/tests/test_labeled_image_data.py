import mock
import numpy
import pytest
from image_representation.implementations.labeled_image_data import LabeledImageData


@pytest.fixture()
@mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
def mock_image_data(mock_image_data):
    mock_image_data.bit_depth = 16
    mock_image_data.number_of_columns = 224
    mock_image_data.number_of_rows = 224
    mock_image_data.number_of_channels = 224
    mock_image_data.color_mode = "RGB"
    mock_image_data.data_source_identifier = "D:\\some\\file"
    mock_image_data.matrix = [1, 2]
    return mock_image_data


class TestLabeledImageData:
    @pytest.mark.parametrize(
        "properties",
        [
            ["bit_depth"],
            ["number_of_rows"],
            ["number_of_columns"],
            ["number_of_channels"],
            ["color_mode"],
            ["data_source_identifier"],
            ["matrix"],
        ],
    )
    def test_image_data_properties(self, mock_image_data, properties):
        labeled_image = LabeledImageData(mock_image_data)
        for property_name in properties:
            assert getattr(labeled_image, property_name) == getattr(mock_image_data, property_name)

    @mock.patch("labels.interfaces.i_label_feature.ILabelFeature", autospec=True)
    def test_add_label_feature(self, mock_label_feature, mock_image_data):
        labeled_image = LabeledImageData(mock_image_data)
        mock_label_feature.name = "Label"
        labeled_image.add_label_feature(mock_label_feature)
        mock_label_feature.name = "Label"
        with pytest.raises(KeyError, match="The name of the label .*"):
            labeled_image.add_label_feature(mock_label_feature)

    @mock.patch("labels.interfaces.i_label_feature.ILabelFeature", autospec=True)
    def test_dict_of_label_feature(self, mock_label_feature, mock_image_data):
        labeled_image = LabeledImageData(mock_image_data)
        label1 = "Label1"
        label2 = "Label2"

        mock_label_feature.name = label1
        labeled_image.add_label_feature(mock_label_feature)
        dict_of_label_features = labeled_image.dict_of_label_features
        assert label1 in dict_of_label_features.keys()
        assert label2 not in dict_of_label_features.keys()

        mock_label_feature.name = label2
        labeled_image.add_label_feature(mock_label_feature)
        dict_of_label_features = labeled_image.dict_of_label_features
        assert len(dict_of_label_features) == 2
        assert label1 in dict_of_label_features.keys()
        assert label2 in dict_of_label_features.keys()
