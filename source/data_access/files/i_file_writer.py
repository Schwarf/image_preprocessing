from abc import ABC

from source.data_access.files.i_file_access import IFileAccess
from source.data_access.interfaces.i_data_sink import IDataSink


class IFileWriter(IDataSink, IFileAccess, ABC):
    pass
