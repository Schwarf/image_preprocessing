import mock
import numpy
import pytest
import tensorflow
from data_access.files.implementations.tensorflow_record_writer import TensorflowRecordWriter


@pytest.fixture()
def full_path(tmp_path):
    path = tmp_path / "test.tf_record"
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

    @mock.patch.object(tensorflow.io, "TFRecordWriter")
    def test_open(self, mock, full_path):
        loader = TensorflowRecordWriter()
        mock.assert_not_called()
        loader.open(full_path)
        mock.assert_called_once()

    @mock.patch.object(tensorflow.io.TFRecordWriter, "write")
    def test_write_is_called(self, mock, full_path):
        loader = TensorflowRecordWriter()
        loader.open(str(full_path))  # use string here since Tf_records to not use pathlib
        mock.assert_not_called()
        raw_data = numpy.array([1, 1, 2, 3, 4]).astype(numpy.int16).tobytes()
        feature = tensorflow.train.Feature(bytes_list=tensorflow.train.BytesList(value=[raw_data]))
        result = {"feature": feature}
        example = tensorflow.train.Example(features=tensorflow.train.Features(feature=result))
        loader.write(example)
        mock.assert_called_once()

    @mock.patch.object(tensorflow.io.TFRecordWriter, "close")
    def test_close_is_called(self, mock, full_path):
        loader = TensorflowRecordWriter()
        loader.open(str(full_path))  # use string here since Tf_records to not use pathlib
        mock.assert_not_called()
        loader.close()
        mock.assert_called_once()
