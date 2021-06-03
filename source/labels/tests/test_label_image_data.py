import mock
import pytest
from image_representation.implementations.labeled_image_data import LabeledImageData
from labels.implementations.label_image_data import LabelImageData
from pure_interface import AdaptionError


class TestLabelImageData:
    def test_set_data_with_None(self):
        label_image_data = LabelImageData()
        data = None
        with pytest.raises(ValueError, match="Image data is 'None'!"):
            label_image_data.set_data(data)

    def test_set_data_with_non_image_data(self):
        label_image_data = LabelImageData()
        data = [1, 2, 3]
        with pytest.raises(AdaptionError, match="Cannot adapt .*"):
            label_image_data.set_data(data)

    @mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
    def test_set_data_with_valid_image_data(self, mock_imaga_data):
        label_image_data = LabelImageData()
        assert label_image_data._labeled_image_data is None
        label_image_data.set_data(mock_imaga_data)
        assert label_image_data._labeled_image_data is not None

    @mock.patch("labels.interfaces.i_label_feature.ILabelFeature", autospec=True)
    def test_assign_label_to_None(self, mock_label):
        label_image_data = LabelImageData()
        with pytest.raises(ValueError, match="Can not assign label, .*"):
            label_image_data.assign(mock_label)

    @mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
    def test_assign_None_label(self, mock_image_data):
        label_image_data = LabelImageData()
        label_image_data.set_data(mock_image_data)
        label = None
        with pytest.raises(ValueError, match="Label is 'None'!"):
            label_image_data.assign(label)

    @mock.patch("image_representation.interfaces.i_image_data.IImageData", autospec=True)
    @mock.patch("labels.interfaces.i_label_feature.ILabelFeature", autospec=True)
    @mock.patch.object(LabeledImageData, "add_label_feature")
    def test_assign_label(self, mock, mock_label, mock_image_data):
        label_image_data = LabelImageData()
        label_image_data.set_data(mock_image_data)
        mock.assert_not_called()
        label_image_data.assign(mock_label)
        mock.assert_called_once()
