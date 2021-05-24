import mock
import pytest
from data_access.files.implementations.tensorflow_record_writer import TensorflowRecordWriter


@pytest.fixture()
def full_path(tmp_path):
    path = tmp_path
    return path


@pytest.fixture()
def invalid_full_path(tmp_path):
    path = "Z:\\invalid\\tests.tfr"
    return path


class TestTensorflowRecordWriter:
    def test_constructor_path_does_not_exist(self, invalid_full_path):
        writer = TensorflowRecordWriter()
        with pytest.raises(ValueError, match="The path provided to .*"):
            writer.open(invalid_full_path)

    @mock.patch.object(TensorflowRecordWriter, "open")
    def test_open(self, mock, full_path):
        loader = TensorflowRecordWriter()
        mock.assert_not_called()
        loader.open(full_path)
        mock.assert_called_once()

    @mock.patch.object(TensorflowRecordWriter, "write")
    def test_read_is_called(self, mock, full_path):
        loader = TensorflowRecordWriter()
        mock.assert_not_called()
        loader.write(None)
        mock.assert_called_once()

    @mock.patch.object(TensorflowRecordWriter, "close")
    def test_close_is_called(self, mock, full_path):
        loader = TensorflowRecordWriter()
        mock.assert_not_called()
        loader.close()
        mock.assert_called_once()
